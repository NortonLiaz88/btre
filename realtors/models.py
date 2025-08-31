from datetime import datetime
from django.db import models


class Realtor(models.Model):
    name = models.CharField(max_length=200)  # type: ignore
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')  # type: ignore
    description = models.TextField(blank=True)  # type: ignore
    email = models.CharField(max_length=50)  # type: ignore
    phone = models.CharField(max_length=20)  # type: ignore
    is_mvp = models.BooleanField(default=False)  # type: ignore
    hire_date = models.DateTimeField(default=datetime.now, blank=True)  # type: ignore

    def __str__(self):
        return self.name