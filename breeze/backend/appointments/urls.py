from django.urls import path
from . import views

urlpatterns = [
    path('appointments/', views.appointment_list),
    path('appointment/', views.appointment),
    path('appointment/<secret_code>', views.appointment_note),
    path('appointment/note/<note_id>', views.appointment_mynote),
]