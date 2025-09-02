"""Module docstring."""

from django.urls import path

from . import api_views

urlpatterns = [
    path("", api_views.Realtors.as_view()),
    path("<int:pk>/", api_views.RealtorDetail.as_view()),
]
