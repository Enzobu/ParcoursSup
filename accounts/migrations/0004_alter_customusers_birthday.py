# Generated by Django 4.2.7 on 2023-12-06 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customusers_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusers',
            name='birthday',
            field=models.DateField(default='2023-12-06', null=True),
        ),
    ]