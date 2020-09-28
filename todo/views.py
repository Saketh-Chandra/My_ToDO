from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *


# Create your views here.
@login_required(login_url='login_page')
def index(request):
    usertask = UserTodo.objects.filter(user=request.user)
    task_forms = user_task_Forms()

    if request.method == 'POST':
        task_forms = user_task_Forms(request.POST)
        if task_forms.is_valid():
            usertask_save = task_forms.save()

            todo_user = UserTodo()
            todo_user.user = request.user
            todo_user.user_tasks = usertask_save
            todo_user.save()
            # print('yah cool')
            return redirect('user_page')
        else:
            pass
    context = {'tasks': usertask, 'task_forms': task_forms}

    return render(request, 'task/list.html', context)


@login_required(login_url='login_page')
def updateTask(request, pk):
    try:
        usertask = UserTask.objects.get(pk=pk)
        task = UserTodo.objects.filter(user=request.user, user_tasks=usertask).first().user_tasks

        # print(task)
        # print('-----')

        form = user_task_Forms(instance=task)
        context = {'form': form}
        if request.method == 'POST':
            form = user_task_Forms(request.POST, instance=task)
            if form.is_valid():
                form.save()
                print('saved')
                return redirect('/')

        return render(request, "task/update_task.html", context)
    except:
        return HttpResponse(f"ID “{pk}” doesn’t exist. Perhaps it was deleted?")


@login_required(login_url='login_page')
def deleteTask(request, pk):
    try:
        item = UserTask.objects.get(id=pk)
        task = UserTodo.objects.filter(user=request.user, user_tasks=item)
        # print(item)
        context = {'item': item}
        if request.method == "POST":
            item.delete()
            task.delete()
            return redirect('user_page')
        return render(request, "task/deletpage.html", context)
    except:
        return HttpResponse(f"ID “{pk}” doesn’t exist. Perhaps it was deleted?")
