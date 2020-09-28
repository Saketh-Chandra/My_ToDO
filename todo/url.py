from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="user_page"),
    path('delete/<str:pk>/', views.deleteTask, name="delete_task"),
    path('update/<str:pk>/', views.updateTask, name="update_task"),
]
