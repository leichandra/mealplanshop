from django import forms  
from recipe.models import Recipe  
import json

class RecipeForm(forms.ModelForm):  
    class Meta:  
        model = Recipe  
        fields = "__all__"  
    def clean(self):
        self.cleaned_data["ingredients"] = json.dumps(self.data.getlist("ingredients"))
        self.instance.ingredient = self.cleaned_data["ingredients"]


   