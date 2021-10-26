from django.urls import path
from . import views

urlpatterns = [
    path('appointment/', views.appointment),
    path('appointment/<note_id>', views.appointment_note),
    path('appointments/', views.appointment_list),
]