from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('delete/<list_id>', views.delete, name="delete"),
    path('cross/<list_id>', views.cross, name="cross"),
    path('edit/<list_id>', views.edit, name="edit"),
]
