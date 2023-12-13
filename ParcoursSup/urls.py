from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from ParcoursSup import settings

urlpatterns = [
    path('', include("ParcoursStup.urls")),
    path('', include("accounts.urls")),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)