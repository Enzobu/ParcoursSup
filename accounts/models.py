from django.contrib.auth.models import AbstractUser
from django.db import models

from ParcoursStup.models import Formation, School

class CustomUsers(AbstractUser):
    user_type = models.CharField(max_length=50)

    ### Étudiant ###
    birthday = models.DateField(default='2023-12-06', null=True)
    report_card = models.FileField(upload_to="report-card", blank=True, null=True)

    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='userSchool', null=True)

class UserFormation(models.Model):
    userStudent = models.ForeignKey(CustomUsers, on_delete=models.CASCADE, related_name='UserFormationUser')
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE, related_name='UserFormationFormation')
    coverLettre = models.TextField()

    def __str__(self):
        return f"{self.userStudent}_{self.formation}"


# cover_letter = models.TextField()
# CV = models.FileField(upload_to="cv", blank=True, null=True)