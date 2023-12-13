from django.contrib import admin
from accounts.models import CustomUsers, UserFormation

# Register your models here.
admin.site.register(CustomUsers)
admin.site.register(UserFormation)
