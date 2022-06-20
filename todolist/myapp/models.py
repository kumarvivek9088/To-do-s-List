from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserTask(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    complete=models.BooleanField(default=False)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title