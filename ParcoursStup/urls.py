from django.urls import path
from .views import index, school_detail

urlpatterns = [
    path('', index, name="index"),
    path('school/<str:slug>/', school_detail, name="school"),
]