from rest_framework import serializers
from .models import UserFollows
from wrestlers.serializers import WrestlerSerializer
from promoters.serializers import PromoterSerializer
from users.serializers import UserSerializer


class UserFollowsSerializer(serializers.ModelSerializer):
    wrestler = WrestlerSerializer()
    promoter = PromoterSerializer()
    user = UserSerializer()

    class Meta:
        model = UserFollows
        fields = '__all__'
