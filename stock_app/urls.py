from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),
    path('inventory/<int:pk>/', views.inventory_detail, name='inventory_detail'),
    path('inventory/new/', views.add_inventory, name='add_inventory'),
    path('inventory/<int:pk>/edit/', views.edit_inventory, name='edit_inventory'),
    path('inventory/<int:pk>/delete/', views.delete_inventory, name='delete_inventory'),
]
