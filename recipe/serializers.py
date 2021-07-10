from rest_framework import serializers

class RecipeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)  
    ingredients = serializers.CharField(max_length=2000)
    instructions = serializers.CharField(max_length=2000)
    id = serializers.IntegerField()