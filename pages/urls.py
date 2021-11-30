#pages/urls.py
from django.urls import path
from .views import homePageView     #metod imported from tab views

urlpatterns = [
    path('',homePageView, name='home'),
]


