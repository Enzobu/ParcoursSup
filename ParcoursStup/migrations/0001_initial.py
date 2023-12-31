# Generated by Django 4.2.7 on 2023-11-30 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ecole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True)),
                ('mail', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=180)),
                ('addresse', models.CharField(max_length=255)),
                ('ville', models.CharField(max_length=80)),
                ('region', models.CharField(max_length=60)),
                ('departement', models.CharField(max_length=50)),
                ('codePostal', models.CharField(max_length=15)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='ecoles')),
            ],
        ),
    ]
