from django.db import models  
from recipe.models import Recipe 
from django.core.validators import MaxLengthValidator
class Agenda(models.Model):  
    date = models.DateField()
    breakfast_recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, blank=True, null=True, related_name='breakfast_agenda_set')
    lunch_recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, blank=True, null=True, related_name='lunch_agenda_set')
    dinner_recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, blank=True, null=True, related_name='dinner_agenda_set')
    
    class Meta:  
        db_table = "agenda"  