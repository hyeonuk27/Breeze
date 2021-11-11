from django.urls import path
from . import views

urlpatterns = [
    path('appointment/', views.appointment),
    path('appointment/<secret_code>', views.appointment_note),
    path('appointment/note/<note_id>', views.appointment_mynote),
    path('appointments/', views.appointment_list),
]