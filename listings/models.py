"""Module docstring."""

from datetime import datetime

from django.db import models

from realtors.models import Realtor


class Listing(models.Model):
    realtor = models.ForeignKey(
        Realtor, on_delete=models.DO_NOTHING)  # type: ignore
    title = models.CharField(max_length=200)  # type: ignore
    address = models.CharField(max_length=200)  # type: ignore
    city = models.CharField(max_length=100)  # type: ignore
    state = models.CharField(max_length=100)  # type: ignore
    zipcode = models.CharField(max_length=20)  # type: ignore
    description = models.TextField(blank=True)  # type: ignore
    price = models.IntegerField()  # type: ignore
    bedrooms = models.IntegerField()  # type: ignore
    bathrooms = models.DecimalField(
        max_digits=2, decimal_places=1)  # type: ignore
    garage = models.IntegerField(default=0)  # type: ignore
    sqft = models.IntegerField()  # type: ignore
    lot_size = models.DecimalField(
        max_digits=5, decimal_places=1)  # type: ignore
    is_published = models.BooleanField(default=True)  # type: ignore
    list_date = models.DateTimeField(
        default=datetime.now, blank=True)  # type: ignore
    photo_main = models.ImageField(
        upload_to="photos/%Y/%m/%d/", blank=True
    )  # type: ignore
    photo_1 = models.ImageField(
        upload_to="photos/%Y/%m/%d/", blank=True
    )  # type: ignore
    photo_2 = models.ImageField(
        upload_to="photos/%Y/%m/%d/", blank=True
    )  # type: ignore
    photo_3 = models.ImageField(
        upload_to="photos/%Y/%m/%d/", blank=True
    )  # type: ignore
    photo_4 = models.ImageField(
        upload_to="photos/%Y/%m/%d/", blank=True
    )  # type: ignore
    photo_5 = models.ImageField(
        upload_to="photos/%Y/%m/%d/", blank=True
    )  # type: ignore
    photo_6 = models.ImageField(
        upload_to="photos/%Y/%m/%d/", blank=True
    )  # type: ignore

    def __str__(self) -> str:
        return str(self.title)
