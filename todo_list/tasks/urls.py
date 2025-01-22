from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('tags/', views.tag_list, name='tag_list'),
    path('task/add/', views.add_task, name='add_task'),
    path('task/<int:pk>/edit/', views.edit_task, name='edit_task'),
    path('task/<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('task/<int:pk>/toggle/', views.toggle_task_status, name='toggle_task_status'),
    path('tag/add/', views.add_tag, name='add_tag'),
    path('tag/<int:pk>/edit/', views.edit_tag, name='edit_tag'),
    path('tag/<int:pk>/delete/', views.delete_tag, name='delete_tag'),
]
