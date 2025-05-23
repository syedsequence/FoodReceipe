from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, SubCategory, Receipe, Ingredient
from .serializers import CategorySerializer, SubCategorySerializer, ReceipeSerializer, IngredientSerializer

# Swagger imports
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.http import JsonResponse

def home(request):
    return JsonResponse({'message': 'Hello from API'})


# -------------------
# Category Views
# -------------------

@swagger_auto_schema(method='get', responses={200: CategorySerializer(many=True)})
@swagger_auto_schema(method='post', request_body=CategorySerializer, responses={201: CategorySerializer})
@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['put', 'patch'], request_body=CategorySerializer)
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        serializer = CategorySerializer(category, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -------------------
# SubCategory Views
# -------------------

@swagger_auto_schema(method='get', responses={200: SubCategorySerializer(many=True)})
@swagger_auto_schema(method='post', request_body=SubCategorySerializer, responses={201: SubCategorySerializer})
@api_view(['GET', 'POST'])
def subcategory_list(request):
    if request.method == 'GET':
        subcategories = SubCategory.objects.all()
        serializer = SubCategorySerializer(subcategories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['put', 'patch'], request_body=SubCategorySerializer)
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def subcategory_detail(request, pk):
    try:
        subcategory = SubCategory.objects.get(pk=pk)
    except SubCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubCategorySerializer(subcategory)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        serializer = SubCategorySerializer(subcategory, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        subcategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -------------------
# Receipe Views
# -------------------

@swagger_auto_schema(method='get', responses={200: ReceipeSerializer(many=True)})
@swagger_auto_schema(method='post', request_body=ReceipeSerializer, responses={201: ReceipeSerializer})
@api_view(['GET', 'POST'])
def receipe_list(request):
    if request.method == 'GET':
        receipes = Receipe.objects.all()
        serializer = ReceipeSerializer(receipes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReceipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['put', 'patch'], request_body=ReceipeSerializer)
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def receipe_detail(request, pk):
    try:
        receipe = Receipe.objects.get(pk=pk)
    except Receipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReceipeSerializer(receipe)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        serializer = ReceipeSerializer(receipe, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        receipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -------------------
# Ingredient Views
# -------------------

@swagger_auto_schema(method='get', responses={200: IngredientSerializer(many=True)})
@swagger_auto_schema(method='post', request_body=IngredientSerializer, responses={201: IngredientSerializer})
@api_view(['GET', 'POST'])
def ingredient_list(request):
    if request.method == 'GET':
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['put', 'patch'], request_body=IngredientSerializer)
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def ingredient_detail(request, pk):
    try:
        ingredient = Ingredient.objects.get(pk=pk)
    except Ingredient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        serializer = IngredientSerializer(ingredient, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
