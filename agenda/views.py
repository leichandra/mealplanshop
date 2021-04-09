from django.shortcuts import render, redirect 
from agenda.models import Agenda
from agenda.forms import AgendaForm
from recipe.models import Recipe  
import logging
logger = logging.getLogger(__name__)

# from recipe.forms import RecipeForm  
# from recipe.models import Recipe  

# Create your views here.  
# def create(request):  
#     if request.method == "POST":  
#         form = RecipeForm(request.POST)  
#         if form.is_valid():  
#             try:  
#                 form.save()  
#                 return redirect('/recipes')  
#             except:  
#                 pass  
#     else:  
#         form = RecipeForm()  
#     return render(request,'recipe/create.html',{'form':form})  

def index(request):  
    logger.warn("HI THERE")
    agendas = Agenda.objects.all()  
    return render(request,"agenda/index.html",{'agendas':agendas})  

def create(request):  
    if request.method == "POST":  
        form = AgendaForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/calendar')  
            except:  
                pass  
    else:  
        form = AgendaForm()  
    return render(request,'agenda/create.html',{'form':form})  

def edit(request, id):  
    agenda = Agenda.objects.get(id=id)  
    recipes = Recipe.objects.all()  
    return render(request,'agenda/edit.html', {'agenda':agenda, 'recipes':recipes})  

def update(request, id):  
    agenda = Agenda.objects.get(id=id)  
    form = AgendaForm(request.POST, instance = agenda)   
    logger.warn("Is valid? " + str(form.is_valid()))
    if form.is_valid():  
        form.save()  
        return redirect("/calendar")  
    recipes = Recipe.objects.all() 
    # logger.warn(str(form.non_field_errors))
    # logger.warn(str(form))
    # logger.warn(str(form.lunch_recipe_id.errors))
    # logger.warn("That is all the errors")
    # logger.warn(str(form.cleaned_data['breakfast_recipe'].errors))
    logger.warn(str(request.POST))
    return render(request, 'agenda/edit.html', {'agenda':agenda, 'recipes':recipes, 'form':form,})  
    
def destroy(request, id):  
    agenda = Agenda.objects.get(id=id)  
    agenda.delete()  
    return redirect("/calendar")  