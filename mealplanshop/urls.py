"""mealplanshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from recipe import views as recipeViews        
from agenda import views as agendaViews

urlpatterns = [
    path('calendar/', agendaViews.index, name='calendar'),
    path('calendar/create', agendaViews.create, name='createcalendar'),
    path('calendar/edit/<int:id>', agendaViews.edit),  
    path('calendar/update/<int:id>', agendaViews.update), 
    path('calendar/delete/<int:id>', agendaViews.destroy),
    path('shoppinglists/', views.shoppinglists, name='shoppinglists'),
    path('nutrition/', views.nutrition, name='nutrition'),
    path('', views.index, name='index'),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', views.profile, name='profile'),
    path('recipes/create', recipeViews.create),  
    path('recipes/', recipeViews.index, name='recipes'),  
    path('recipes/edit/<int:id>', recipeViews.edit),  
    path('recipes/update/<int:id>', recipeViews.update),  
    path('recipes/delete/<int:id>', recipeViews.destroy), 
    path('recipes_old/', views.recipes, name='oldRecipes'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

