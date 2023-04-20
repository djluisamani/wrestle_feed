from rest_framework import serializers
from .models import Promoter


class PromoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promoter
        fields = '__all__'
