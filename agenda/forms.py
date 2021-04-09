from django import forms  
from agenda.models import Agenda  
from mealplanshop import settings
class AgendaForm(forms.ModelForm):
    date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = Agenda
        fields = "__all__"

