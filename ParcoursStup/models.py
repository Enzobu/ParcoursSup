from django.db import models

"""
from django.db import models
from django.contrib.auth.models import AbstractUser

class Ecole(AbstractUser):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    mail = models.CharField(max_length=250)
    password = models.CharField(max_length=20)
    adresse = models.CharField(max_length=150)
    ville = models.CharField(max_length=80)
    region = models.CharField(max_length=100)
    departement = models.CharField(max_length=100)
    codePostal = models.CharField(max_length=15)
    secteur = models.CharField(max_length=50)

class Formation(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    duree = models.IntegerField()
    diplome = models.CharField(max_length=120)
    competencesRequises = models.TextField()
    cout = models.DecimalField(max_digits=10, decimal_places=2)
    ecoles = models.ManyToManyField(Ecole)

class Eleve(AbstractUser):
    nom = models.CharField(max_length=80)
    prenom = models.CharField(max_length=80)
    mail = models.CharField(max_length=250)
    password = models.CharField(max_length=20)
    adresse = models.CharField(max_length=200)
    ville = models.CharField(max_length=80)
    departement = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    codePostal = models.CharField(max_length=15)
    ecoles = models.ForeignKey(Ecole, on_delete=models.CASCADE)
    ecoles = models.ManyToManyField(Ecole)
    formations = models.ManyToManyField(Formation)

"""