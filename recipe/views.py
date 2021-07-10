from django.shortcuts import render, redirect  
from recipe.forms import RecipeForm  
from recipe.models import Recipe  
from django.http import JsonResponse
from recipe.serializers import RecipeSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.http import HttpResponse
import json

# Create your http views here.  
def create(request):  
    if request.method == "POST":  
        form = RecipeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/recipes')  
            except:  
                pass  
    else:  
        form = RecipeForm()  
    return render(request,'recipe/create.html',{'form':form})  

def update(request, id):  
    recipe = Recipe.objects.get(id=id)  
    form = RecipeForm(request.POST, instance = recipe)  
    if form.is_valid():  
        form.save()  
        return redirect("/recipes")  
    return render(request, 'recipe/edit.html', {'recipe': recipe}) 


def index(request):  
    recipes = Recipe.objects.all()  
    return render(request,"recipe/index.html",{'recipes':recipes})  

def edit(request, id):  
    recipe = Recipe.objects.get(id=id)  
    ingredients = json.loads(recipe.ingredients)
    return render(request,'recipe/edit.html', {'recipe':recipe, 'ingredients':ingredients})  
    
def destroy(request, id):  
    recipe = Recipe.objects.get(id=id)  
    recipe.delete()  
    return redirect("/recipes")  

# Create your API views here.  
@csrf_exempt
@api_view(['GET', 'POST'])
def apiList(request):  
    if request.method == "POST": 
        return apiCreate(request)

    recipes = Recipe.objects.all()  
    newlist = [RecipeSerializer(r).data for r in recipes]
    return JsonResponse({'recipes':newlist})
    
def apiCreate(request):
    recipe = Recipe()
    data = request.data
    recipe.name = data["name"]
    recipe.ingredients = data["ingredients"]
    recipe.instructions = data["directions"]
    try:
        recipe.full_clean() 
        try:  
            recipe.save()  
            serializedRecipe = RecipeSerializer(recipe).data 
            return JsonResponse(serializedRecipe) 
        except: 
            return Response({"error": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)  
    except ValidationError as e:
        return Response({"error": "Validation failed for recipe"}, status=status.HTTP_400_BAD_REQUEST) 

@csrf_exempt
@api_view(['GET', 'PATCH', 'DELETE'])
def apiGet(request, id):
    
    if request.method == "PATCH": 
        return apiPatch(request, id)
    elif request.method == "DELETE":
        return apiDelete(request, id)
    else:
        recipe = Recipe.objects.get(id=id)
        serializedRecipe = RecipeSerializer(recipe).data 
        return JsonResponse(serializedRecipe)
     

def apiDelete(request, id):  
    recipe = Recipe.objects.get(id=id)  
    recipe.delete()  
    return HttpResponse(status=204)
    
def apiPatch(request, id):
    # the function apiPatch passes 2 things: request & id
    data = request.data
    # a variable data is equal to the request data, which is serialized JSON
    recipe = Recipe.objects.get(id=id)
    # a variable recipe is equal to the getting of the recipes from the database given the id
    recipe.name = data["name"]
    # the variable recipe.name is equal to the request data trying to access the "name" value in the dictionary
    recipe.ingredients = data["ingredients"]
    # this variable is equal to the request data trying to access the "ingredients" value in the dictionary
    recipe.instructions = data["instructions"]
    # this variable is equal to the request data accessing the "instructions" value in the dictionary
    try:
        recipe.full_clean() 
        try:  
            recipe.save()  
            serializedRecipe = RecipeSerializer(recipe).data 
            return JsonResponse(serializedRecipe) 
        except: 
            return Response({"error": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)  
    except ValidationError as e:
        return Response({"error": "Validation failed for recipe"}, status=status.HTTP_400_BAD_REQUEST) 