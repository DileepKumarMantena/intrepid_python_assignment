# Generated by Django 5.0.6 on 2024-06-12 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intrepid_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboarditem',
            name='user',
        ),
    ]
