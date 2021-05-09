from django.urls import path
from .views import sayhi

urlpatterns = [
    path('sayhi/<str:yourname>/', sayhi)
]