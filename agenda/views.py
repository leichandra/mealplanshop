from django.shortcuts import render, redirect 
from agenda.models import Agenda
from agenda.forms import AgendaForm
from recipe.models import Recipe  
from datetime import date
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.core.exceptions import ValidationError
from agenda.serializers import AgendaSerializer
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
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

@csrf_exempt
@api_view(['GET', 'POST'])
def apiList(request):  
    if request.method == "POST": 
        return apiCreate(request)

    agendas = Agenda.objects.all()  
    newlist = [AgendaSerializer(r).data for r in agendas]
    return JsonResponse({'agendas':newlist})

def apiCreate(request):
    agenda = Agenda()
    data = request.data
    # take meal date and put in on the agenda
    agenda.date = date.fromisoformat(data["date"])
    agenda.breakfast_recipe_id = data["breakfast_recipe"]
    agenda.lunch_recipe_id = data["lunch_recipe"]
    agenda.dinner_recipe_id = data["dinner_recipe"]
    try:
        agenda.full_clean() 
        try:  
            agenda.save()  
            serializedAgenda = AgendaSerializer(agenda).data 
            return JsonResponse(serializedAgenda) 
            return JsonResponse({})
        except: 
            return Response({"error": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)  
    except ValidationError as e:
        return Response({"error": "Validation failed for agenda"}, status=status.HTTP_400_BAD_REQUEST) 

@csrf_exempt
@api_view(['GET', 'PATCH', 'DELETE'])
def apiGet(request, id):
    if request.method == "PATCH": 
        return apiPatch(request, id)
    elif request.method == "DELETE":
        return apiDelete(request, id)
    agenda = Agenda.objects.get(id=id)
    serializedAgenda = AgendaSerializer(agenda).data 
    return JsonResponse(serializedAgenda)


def apiPatch(request, id):
    data = request.data
    agenda = Agenda.objects.get(id=id)
    agenda.date = date.fromisoformat(data["date"])
    agenda.breakfast_recipe_id = data["breakfast_recipe"]
    agenda.lunch_recipe_id = data["lunch_recipe"]
    agenda.dinner_recipe_id = data["dinner_recipe"]
    try:
        agenda.full_clean() 
        try:  
            agenda.save()  
            serializedAgenda = AgendaSerializer(agenda).data 
            return JsonResponse(serializedAgenda) 
        except: 
            return Response({"error": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)  
    except ValidationError as e:
        return Response({"error": "Validation failed for recipe"}, status=status.HTTP_400_BAD_REQUEST) 


def apiDelete(request, id):  
    agenda = Agenda.objects.get(id=id)  
    agenda.delete()  
    return HttpResponse(status=204)



