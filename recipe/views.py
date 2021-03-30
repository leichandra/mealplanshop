from django.shortcuts import render, redirect  
from recipe.forms import RecipeForm  
from recipe.models import Recipe  

# Create your views here.  
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

def index(request):  
    recipes = Recipe.objects.all()  
    return render(request,"recipe/index.html",{'recipes':recipes})  

def edit(request, id):  
    recipe = Recipe.objects.get(id=id)  
    return render(request,'recipe/edit.html', {'recipe':recipe})  

def update(request, id):  
    recipe = Recipe.objects.get(id=id)  
    form = RecipeForm(request.POST, instance = recipe)  
    if form.is_valid():  
        form.save()  
        return redirect("/recipes")  
    return render(request, 'recipe/edit.html', {'recipe': recipe})  
    
def destroy(request, id):  
    recipe = Recipe.objects.get(id=id)  
    recipe.delete()  
    return redirect("/recipes")  