# Generated by Django 4.2.7 on 2023-12-09 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ParcoursStup', '0018_formation_slug'),
        ('accounts', '0008_remove_customusers_formation'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFormation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coverLettre', models.TextField()),
                ('formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserFormationFormation', to='ParcoursStup.formation')),
                ('userStudent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserFormationUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]