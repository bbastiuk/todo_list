from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.shortcuts import get_object_or_404, redirect
from .models import Task, Tag
from .forms import TaskForm, TagForm

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.all().order_by('is_done', '-datetime')

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/add_task.html'
    success_url = reverse_lazy('tasks:task_list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/edit_task.html'
    success_url = reverse_lazy('tasks:task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/confirm_delete.html'
    success_url = reverse_lazy('tasks:task_list')

class TaskToggleStatusView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect('tasks:task_list')

class TagListView(ListView):
    model = Tag
    template_name = 'tasks/tag_list.html'
    context_object_name = 'tags'

class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'tasks/add_tag.html'
    success_url = reverse_lazy('tasks:tag_list')

class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'tasks/edit_tag.html'
    success_url = reverse_lazy('tasks:tag_list')

class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'tasks/confirm_delete.html'
    success_url = reverse_lazy('tasks:tag_list')
