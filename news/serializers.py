from rest_framework import serializers
from .models import News
from wrestlers.serializers import WrestlerSerializer
from promoters.serializers import PromoterSerializer


class NewsSerializer(serializers.ModelSerializer):
    wrestler = WrestlerSerializer()
    promoter = PromoterSerializer()

    class Meta:
        model = News
        fields = '__all__'
