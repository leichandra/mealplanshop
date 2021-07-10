from rest_framework import serializers
from agenda.models import Agenda

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ["id", "date", "breakfast_recipe", "lunch_recipe", "dinner_recipe"]

