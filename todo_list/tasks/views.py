from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Tag
from .forms import TaskForm, TagForm

def task_list(request):
    tasks = Task.objects.all().order_by('is_done', '-datetime')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'tasks/tag_list.html', {'tags': tags})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('tasks:task_list')

def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect('tasks:task_list')

def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:tag_list')
    else:
        form = TagForm()
    return render(request, 'tasks/add_tag.html', {'form': form})

def edit_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('tasks:tag_list')
    else:
        form = TagForm(instance=tag)
    return render(request, 'tasks/edit_tag.html', {'form': form})

def delete_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    tag.delete()
    return redirect('tasks:tag_list')
