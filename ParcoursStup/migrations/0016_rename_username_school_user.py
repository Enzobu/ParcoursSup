# Generated by Django 4.2.7 on 2023-12-09 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ParcoursStup', '0015_alter_school_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='username',
            new_name='user',
        ),
    ]