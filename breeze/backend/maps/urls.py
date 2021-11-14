from django.urls import path
from . import views

urlpatterns = [
    path('middle/', views.get_middle),
    path('store/<int:category_id>/<int:filter_id>/', views.get_store),
]