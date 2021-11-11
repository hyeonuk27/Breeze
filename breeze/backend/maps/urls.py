from django.urls import path
from . import views

urlpatterns = [
    path('middle/', views.get_middle),
    path('store/<int:category_id>/<int:filter_id>/', views.get_store),
    path('test/', views.store_info),
    path('alcohol/', views.get_alcohol),
    path('data/', views.data_integration),
    path('rate/', views.get_rate),
]