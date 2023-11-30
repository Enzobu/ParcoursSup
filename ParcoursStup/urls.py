from django.conf.urls.static import static
from django.urls import path
from .views import index, school_detail
from ParcoursSup import settings

urlpatterns = [
    path('', index, name="index"),
    path('school/<str:slug>/', school_detail, name="school"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)