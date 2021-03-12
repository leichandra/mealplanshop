# from django.views import generic

# class IndexView(generic.ListView):
#   template_name = 'mealplanshop/index.html'

#   def get_queryset(self):
#     return []


from django.http import HttpResponse
from django.shortcuts import render
import datetime

def index(request):
  # now = datetime.datetime.now()
  # html = "<html><body>It is now %s.</body></html>" % now
  # return HttpResponse(html)
  return render(request, 'mealplanshop/index.html')

def profile(request):
  return render(request, 'mealplanshop/profile.html')

def calendar(request):
  return render(request, 'mealplanshop/calendar.html')

def recipes(request):
  return render(request, 'mealplanshop/recipes.html')

def shoppinglists(request):
  return render(request, 'mealplanshop/shoppinglists.html')

def nutrition(request):
  return render(request, 'mealplanshop/nutrition.html')