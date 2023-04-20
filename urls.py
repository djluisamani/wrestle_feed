from django.urls import path
from . import views

urlpatterns = [
    path('wrestle_feed/', views.my_view, name='my_view'),
]
