from django.db import models
from django.urls import reverse

"""from django.contrib.auth.models import AbstractUser

class Ecole(models.Model):
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

class Eleve(models.Model):
    nom = models.CharField(max_length=80)
    prenom = models.CharField(max_length=80)
    mail = models.CharField(max_length=250)
    password = models.CharField(max_length=20)
    adresse = models.CharField(max_length=200)
    ville = models.CharField(max_length=80)
    departement = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    codePostal = models.CharField(max_length=15)
    # ecoles = models.ForeignKey(Ecole, on_delete=models.CASCADE)
    # ecoles = models.ManyToManyField(Ecole)
    # formations = models.ManyToManyField(Formation)

"""

class School(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=126)
    mail = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=80)
    region = models.CharField(max_length=60)
    department = models.CharField(max_length=50)
    zipCode = models.IntegerField()
    picture = models.ImageField(upload_to="school", blank=True, null=True)

    def __str__(self):
        return f"School_{self.name}"
    
    def get_absolute_url(self):
        return f"school/{self.slug}/"
    
    def get_complete_address(self):
        return f"{self.address}, {self.zipCode} {self.city}"
    
