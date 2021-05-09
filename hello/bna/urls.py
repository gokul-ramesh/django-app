from django.urls import path
from .views import books,display

urlpatterns = [
    path('book/', books),
    path('display/',display),
]