from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUsers(AbstractUser):
    user_type = models.CharField(max_length=50)

    ### Étudiant ###
    birthday = models.DateField(default='2023-12-06', null=True)
    report_card = models.FileField(upload_to="report-card", blank=True, null=True)
    



# cover_letter = models.TextField()
# CV = models.FileField(upload_to="cv", blank=True, null=True)