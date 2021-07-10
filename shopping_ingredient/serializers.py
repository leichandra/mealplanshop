from rest_framework import serializers
from shopping_ingredient.models import ShoppingIngredient

class ShoppingIngredientSerializer(serializers.Serializer):
    class Meta:
        model = ShoppingIngredient
        fields = ["id", "name", "store", "created_at", "updated_at"]