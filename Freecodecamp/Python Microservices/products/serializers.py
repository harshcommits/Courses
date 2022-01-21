from rest_framework import serializers

class ProductSerializer(serialize):
    class Meta:
        model = Product
        fields = '__all__'