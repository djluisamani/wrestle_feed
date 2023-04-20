from rest_framework import generics
from .models import Promoter, Wrestler, User, News, UserFollows
from .serializers import PromoterSerializer, WrestlerSerializer, UserSerializer, NewsSerializer, UserFollowsSerializer


class PromoterList(generics.ListCreateAPIView):
    queryset = Promoter.objects.all()
    serializer_class = PromoterSerializer


class PromoterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Promoter.objects.all()
    serializer_class = PromoterSerializer


class WrestlerList(generics.ListCreateAPIView):
    queryset = Wrestler.objects.all()
    serializer_class = WrestlerSerializer


class WrestlerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wrestler.objects.all()
    serializer_class = WrestlerSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class UserFollowsList(generics.ListCreateAPIView):
    queryset = UserFollows.objects.all()
    serializer_class = UserFollowsSerializer


class UserFollowsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserFollows.objects.all()
    serializer_class = UserFollowsSerializer
