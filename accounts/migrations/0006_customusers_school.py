# Generated by Django 4.2.7 on 2023-12-09 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ParcoursStup', '0017_remove_school_user'),
        ('accounts', '0005_rename_usertype_customusers_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusers',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userSchool', to='ParcoursStup.school'),
        ),
    ]
