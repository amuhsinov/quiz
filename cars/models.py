from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    car = models.ImageField(upload_to='cars/', default='')
    name = models.TextField()
    fk_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
