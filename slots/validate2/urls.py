from django.urls import path
from . import views

urlpatterns = [
    path('', views.validate_numeric_entity, name='numeric')
]