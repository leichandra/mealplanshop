from django.db import models  
from django.core.validators import MaxLengthValidator
class Recipe(models.Model):  
    name = models.CharField(max_length=100)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ingredients = models.TextField(max_length=2000, blank=True,
                                   validators=[MaxLengthValidator(2000)])
    instructions = models.TextField(max_length=2000, blank=True,
                                   validators=[MaxLengthValidator(2000)])
    class Meta:  
        db_table = "recipe"  