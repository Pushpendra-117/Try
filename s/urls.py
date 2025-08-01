from django.urls import path
from s import views

urlpatterns = [
    path('', views.index, name='index'),

]
