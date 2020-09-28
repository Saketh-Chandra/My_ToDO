from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="user_page"),
    path('delet_task/<str:pk>/', views.deleteTask, name="delete_task"),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
]
