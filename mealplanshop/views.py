# from django.views import generic

# class IndexView(generic.ListView):
#   template_name = 'mealplanshop/index.html'

#   def get_queryset(self):
#     return []


from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import redirect, render
import datetime
import calendar as calendar2
import urllib.parse

def index(request):
  # now = datetime.datetime.now()
  # html = "<html><body>It is now %s.</body></html>" % now
  # return HttpResponse(html)
  # return render(request, 'mealplanshop/index.html')
  return redirect('accounts/login')

def profile(request):
  return render(request, 'mealplanshop/profile.html')

def calendar(request):
  myCal = calendar2.HTMLCalendar(calendar2.SUNDAY)
  myMonth = myCal.formatmonth(2009, 7)
  return render(request, 'mealplanshop/calendar.html', {"month": myMonth})

def recipes(request):
  return render(request, 'mealplanshop/recipes.html')

def shoppinglists(request):
  return render(request, 'mealplanshop/shoppinglists.html')

def nutrition(request):
  melatoninLink = 'https://www.amazon.com/s?k={}'.format('melatonin')
  magnesiumLink = 'https://www.amazon.com/s?k={}'.format('magnesium')
  chamomileTeaUrlSafe = urllib.parse.quote('chamomile tea')
  chamomileTeaLink = 'https://www.amazon.com/s?k={}'.format(chamomileTeaUrlSafe)
  return render(request, 'mealplanshop/nutrition.html', {"melatonin": melatoninLink, "magnesium": magnesiumLink, "chamomileTeaLink": chamomileTeaLink})
  
  
  

