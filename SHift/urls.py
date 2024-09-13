from django.urls import path
from . import views

urlpatterns = [
    path('shifts/', views.shift_list, name='shift_list'),
    path('shifts/create/', views.shift_create, name='shift_create'),
    path('shifts/<int:id>/', views.shift_detail, name='shift_detail'),
    path('shifts/<int:id>/update/', views.shift_update, name='shift_update'),
    path('shifts/<int:id>/delete/', views.shift_delete, name='shift_delete'),
]

