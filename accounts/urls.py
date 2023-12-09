from django.urls import path
from accounts.views import signup, logout_user, login_user
from django.conf.urls.static import static
from ParcoursSup import settings

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)