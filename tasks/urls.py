from django.urls import path
from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskToggleStatusView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

app_name = 'tasks'

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('task/add/', TaskCreateView.as_view(), name='add_task'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='edit_task'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete_task'),
    path('task/<int:pk>/toggle/', TaskToggleStatusView.as_view(), name='toggle_task_status'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('tag/add/', TagCreateView.as_view(), name='add_tag'),
    path('tag/<int:pk>/edit/', TagUpdateView.as_view(), name='edit_tag'),
    path('tag/<int:pk>/delete/', TagDeleteView.as_view(), name='delete_tag'),
]
