from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import *
from .models import *


# views.


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
            message = "successfully created task!"
            messages.success(request, message)
            return redirect('user_page')
        else:
            # print('error')
            message = "to created task!"
            messages.error(request, message)
    context = {'tasks': usertask, 'task_forms': task_forms}

    return render(request, 'todo/index.html', context)


@login_required(login_url='login_page')
def updateTask(request, pk):
    try:
        usertask = UserTask.objects.get(pk=pk)
        task = UserTodo.objects.filter(user=request.user, user_tasks=usertask).first().user_tasks
        # print(task)
        form = user_task_Forms(instance=task)
        context = {'form': form}
        if request.method == 'POST':
            form = user_task_Forms(request.POST, instance=task)
            if form.is_valid():
                form.save()
                message = "successfully updated task!"
                messages.success(request, message)
                # print('saved')
                return redirect('user_page')

        return render(request, "todo/update_page.html", context)

    except:
        return HttpResponse(f" <h1>404 Error</h1> <h3>page update/{pk} doesn’t exist. Perhaps it was deleted?</h3>")


@login_required(login_url='login_page')
def deleteTask(request, pk):
    try:
        item = UserTask.objects.get(id=pk)
        print(item.task_name)
        task = UserTodo.objects.filter(user=request.user, user_tasks=item)
        context = {'item': item}
        if request.method == "POST":
            item.delete()
            task.delete()
            message = "successfully deleted task!"
            messages.success(request, message)
            return redirect('user_page')
        return render(request, "todo/delete_page.html", context)
    except:
        return HttpResponse(f"<h1>404 Error</h1> <h3>page delete/{pk} doesn’t exist. Perhaps it was deleted?</h3>")
