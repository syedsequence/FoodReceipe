# models.py

from django.db import models

class Category(models.Model):
    category_code = models.CharField(max_length=50, unique=True) 
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    category_reference = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    subcategory_code = models.CharField(max_length=50, unique=True)  
    subcategory_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subcategory_name

class Ingredient(models.Model):
    ingredient_code = models.CharField(max_length=50, unique=True)
    ingredient_name = models.CharField(max_length=100)

    def __str__(self):
        return self.ingredient_name

class Receipe(models.Model):
    category_reference = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    subcategory_reference = models.ForeignKey(SubCategory, null=True, on_delete=models.SET_NULL)
    receipe_code = models.CharField(max_length=50, unique=True) 
    receipe_name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField('Ingredient', through='ReceipeIngredient')

    def __str__(self):
        return self.receipe_name

class ReceipeIngredient(models.Model):
    recipe = models.ForeignKey(Receipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    wastage = models.FloatField()

    def __str__(self):
        return f"{self.ingredient.ingredient_name} for {self.recipe.receipe_name}"
