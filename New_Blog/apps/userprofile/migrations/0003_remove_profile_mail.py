# Generated by Django 3.1 on 2020-08-26 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_profile_mail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='mail',
        ),
    ]