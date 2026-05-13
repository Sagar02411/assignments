from rest_framework import serializers
from .models import EBooksModel

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = EBooksModel
        fields = '__all__'