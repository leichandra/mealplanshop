from django import forms  
from shopping_ingredient.models import ShoppingIngredient  
import json

class ShoppingIngredientForm(forms.ModelForm):  
    class Meta:  
        model = ShoppingIngredient  
        fields = "__all__"  
   