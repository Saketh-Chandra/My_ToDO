from django.db import models
from django.contrib.auth.models import User


# My models here.

class UserTask(models.Model):
    task_name = models.CharField(max_length=100)
    task_complate = models.BooleanField(default=False)
    task_created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name


class UserTodo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_tasks = models.ForeignKey(UserTask, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} {self.user_tasks.task_name}'
