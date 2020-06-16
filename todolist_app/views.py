from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Tasklist
from .forms import Taskform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required()
def todolist(request):
    if request.method == 'POST':
        form = Taskform(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage=request.user
            instance.save()
        messages.success(request, ("New task added successfully"))
        return redirect('todolist')
    else:
        all_list = Tasklist.objects.filter(manage=request.user)
        paginator = Paginator(all_list,5)
        page = request.GET.get('pg')
        all_list = paginator.get_page(page)
        return render(request,'todolist.html',{'all_list' : all_list})

@login_required()
def delete_task(request,task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.error(request, ('OOPS! Not allowed to access'))
    return redirect('todolist')

@login_required()
def edit_task(request,task_id):
    if request.method == 'POST':
        task = Tasklist.objects.get(pk=task_id)
        form = Taskform(request.POST or None , instance=task)
        if form.is_valid():
            form.save()
        messages.success(request, ('Edited task successfully'))
        return redirect('todolist')
    else:
        task_obj= Tasklist.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})

@login_required()
def complete_task(request,task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, ('OOPS! Not allowed to access'))
    return redirect('todolist')

@login_required()
def pending_task(request,task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')

def contact(request):
    context = {'contact_text': 'This Sai Ajay, Welcome to Contact page',
               }
    return render(request, 'contact.html', context)


def about(request):
    context = {'about_text': 'This Sai Ajay, Welcome to About page',
               }
    return render(request, 'about.html', context)

def index(request):
    context = {'index_text': 'This Sai Ajay, Welcome to Index page',
               }
    return render(request, 'index.html', context)

def ajax(request):
    context = {'ajax_text': 'This Sai Ajay, Welcome to Index page',
               }
    return render(request, 'ajax.html', context)