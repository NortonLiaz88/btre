from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.Listings.as_view()),
    path('<int:pk>/', api_views.Listing.as_view()),
]
