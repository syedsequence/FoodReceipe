# serializers.py

from rest_framework import serializers
from .models import Category, SubCategory, Ingredient, Receipe, ReceipeIngredient

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_code', 'category_name']

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['subcategory_code', 'subcategory_name', 'category_reference']

# For output of ingredients (GET)
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['ingredient_code', 'ingredient_name']

# For output of recipe ingredients (GET)
class ReceipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = ReceipeIngredient
        fields = ['ingredient', 'quantity', 'wastage']

# For input of ingredients (POST/PUT/PATCH)
class ReceipeIngredientInputSerializer(serializers.Serializer):
    ingredient = serializers.CharField()  # ingredient_code
    quantity = serializers.IntegerField()
    wastage = serializers.FloatField()

    def validate(self, data):
        if data['wastage'] > data['quantity']:
            raise serializers.ValidationError("Wastage cannot be greater than quantity.")
        return data

# Main Receipe serializer
class ReceipeSerializer(serializers.ModelSerializer):
    category_reference = serializers.CharField()  # category_code
    subcategory_reference = serializers.CharField()  # subcategory_code
    ingredients_data = ReceipeIngredientInputSerializer(many=True, write_only=True)
    ingredients = ReceipeIngredientSerializer(source='receipeingredient_set', many=True, read_only=True)
    category_name = serializers.CharField(source='category_reference.category_name', read_only=True)
    subcategory_name = serializers.CharField(source='subcategory_reference.subcategory_name', read_only=True)

    class Meta:
        model = Receipe
        fields = [
            'id',
            'receipe_code',
            'receipe_name',
            'category_reference',
            'category_name', 
            'subcategory_reference',
            'subcategory_name', 
            'ingredients_data',  
            'ingredients',       
        ]

    def create(self, validated_data):
        category_code = validated_data.pop('category_reference')
        subcategory_code = validated_data.pop('subcategory_reference')
        ingredients_data = validated_data.pop('ingredients_data')

        try:
            category = Category.objects.get(category_code=category_code)
        except Category.DoesNotExist:
            raise serializers.ValidationError({'category_reference': 'Invalid category code.'})

        try:
            subcategory = SubCategory.objects.get(subcategory_code=subcategory_code)
        except SubCategory.DoesNotExist:
            raise serializers.ValidationError({'subcategory_reference': 'Invalid subcategory code.'})

        receipe = Receipe.objects.create(
            category_reference=category,
            subcategory_reference=subcategory,
            **validated_data
        )

        for item in ingredients_data:
            ingredient_code = item['ingredient']
            try:
                ingredient = Ingredient.objects.get(ingredient_code=ingredient_code)
            except Ingredient.DoesNotExist:
                raise serializers.ValidationError({'ingredient': f'Invalid ingredient code: {ingredient_code}'})

            ReceipeIngredient.objects.create(
                recipe=receipe,
                ingredient=ingredient,
                quantity=item['quantity'],
                wastage=item['wastage']
            )

        return receipe

    def update(self, instance, validated_data):
        category_code = validated_data.pop('category_reference', None)
        subcategory_code = validated_data.pop('subcategory_reference', None)
        ingredients_data = validated_data.pop('ingredients_data', None)

        if category_code:
            try:
                category = Category.objects.get(category_code=category_code)
                instance.category_reference = category
            except Category.DoesNotExist:
                raise serializers.ValidationError({'category_reference': 'Invalid category code.'})

        if subcategory_code:
            try:
                subcategory = SubCategory.objects.get(subcategory_code=subcategory_code)
                instance.subcategory_reference = subcategory
            except SubCategory.DoesNotExist:
                raise serializers.ValidationError({'subcategory_reference': 'Invalid subcategory code.'})

        instance.receipe_code = validated_data.get('receipe_code', instance.receipe_code)
        instance.receipe_name = validated_data.get('receipe_name', instance.receipe_name)
        instance.save()

        if ingredients_data is not None:
            ReceipeIngredient.objects.filter(recipe=instance).delete()

            for item in ingredients_data:
                ingredient_code = item['ingredient']
                try:
                    ingredient = Ingredient.objects.get(ingredient_code=ingredient_code)
                except Ingredient.DoesNotExist:
                    raise serializers.ValidationError({'ingredient': f'Invalid ingredient code: {ingredient_code}'})

                ReceipeIngredient.objects.create(
                    recipe=instance,
                    ingredient=ingredient,
                    quantity=item['quantity'],
                    wastage=item['wastage']
                )

        return instance
