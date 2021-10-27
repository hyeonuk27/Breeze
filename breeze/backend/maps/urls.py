from django.urls import path
from . import views

urlpatterns = [
    path('middle/', views.get_middle),
    path('store/<category_id>/<filter_id>/', views.get_store),
    path('test/', views.store_info)
]