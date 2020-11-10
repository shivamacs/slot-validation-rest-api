from django.urls import path
from . import views

urlpatterns = [
    path('', views.validate_finite_values_entity, name='finite_set')
]