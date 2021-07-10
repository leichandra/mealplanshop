from django.db import models  

class ShoppingIngredient(models.Model):  
    name = models.CharField(max_length=100)  
    store = models.CharField(max_length=100, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  
        db_table = "shopping_ingredient"  