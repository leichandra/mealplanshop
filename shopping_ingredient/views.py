from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shopping_ingredient.models import ShoppingIngredient
from shopping_ingredient.serializers import ShoppingIngredientSerializer
from shopping_ingredient.forms import ShoppingIngredientForm

def index(request):  
    if request.method == "POST":  
        updateShoppingList(request)

    forms = []
    ShoppingIngredientForm
    shopping_ingredients = ShoppingIngredient.objects.all()  
    for ingredient in shopping_ingredients:
        forms.append(ShoppingIngredientForm(request.POST, instance = ingredient))

    return render(request, "shopping_ingredient/index.html", { 'shopping_ingredients': shopping_ingredients, 'forms': forms })  

def updateShoppingList(request):
    form = ShoppingIngredientForm(request.POST)  
    if form.is_valid():  
        try:  
            form.save()  
        except:  
            pass  

@csrf_exempt
@api_view(['POST'])
def apiPost(request):
    data = request.data

    shopping_ingredient = ShoppingIngredient()
    shopping_ingredient.name = data["name"]

    try:
        shopping_ingredient.full_clean() 
        try:  
            shopping_ingredient.save()  
            return JsonResponse(ShoppingIngredientSerializer(shopping_ingredient).data) 
        except: 
            return Response({"error": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)  
    except ValidationError as e:
        return Response({"error": "Validation failed for recipe"}, status=status.HTTP_400_BAD_REQUEST) 
  

