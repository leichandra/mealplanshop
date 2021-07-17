from django.core.exceptions import ValidationError
from django.forms import modelformset_factory
from django.http import JsonResponse
from django.shortcuts import render, redirect 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from shopping_ingredient.models import ShoppingIngredient
from shopping_ingredient.serializers import ShoppingIngredientSerializer
from shopping_ingredient.forms import ShoppingIngredientForm

def index(request):  
    if request.method == "POST":  
        return updateShoppingList(request)
        
    # forms = []
    # shopping_ingredients = ShoppingIngredient.objects.all()  
    # for ingredient in shopping_ingredients:
    #     forms.append(ShoppingIngredientForm(request.POST, instance = ingredient))

    ShoppingIngredientFormSet = modelformset_factory(ShoppingIngredient, fields=('name', 'store'))
    formset = ShoppingIngredientFormSet()

    return render(request, "shopping_ingredient/index.html", { 'formset': formset })  

def updateShoppingList(request):
    ShoppingIngredientFormSet = modelformset_factory(ShoppingIngredient, fields=('name', 'store'), extra=1)
    formset = ShoppingIngredientFormSet(request.POST)
    formset.save()  
    formset = ShoppingIngredientFormSet()
    return render(request, "shopping_ingredient/index.html", { 'formset': formset })  

def delete(request, id):
    shopping_ingredient = ShoppingIngredient.objects.get(id=id)  
    shopping_ingredient.delete()  
    return redirect("/shopping_ingredients") 

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
  

