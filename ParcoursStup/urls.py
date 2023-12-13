from django.urls import path
from .views import index, school_detail, school_list, postuler, formation, add_formation, remove_formation

urlpatterns = [
    path('', index, name="index"),
    path('school', school_list, name="school_list"),
    path('school/<str:slug>/', school_detail, name="school_detail"),
    path('school/<str:slug>/<str:formation>/', postuler, name="postuler"),
    path('formation', formation, name="formation"),
    path('add-formation', add_formation, name="add_formation"),
    path('remove-formation/<str:slug>/', remove_formation, name="remove_formation"),
    path('postuler/<str:slug>/', postuler, name="postuler"),
]