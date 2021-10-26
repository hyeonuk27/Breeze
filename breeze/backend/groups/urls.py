from django.urls import path
from . import views

urlpatterns = [
    path('group/', views.group_create),
    path('groups/', views.groups),
    path('group/<group_id>/', views.group_delete),
]