# Generated by Django 5.0.6 on 2024-06-12 16:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_email', models.EmailField(max_length=254)),
                ('customer_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('booking_date', models.DateTimeField()),
                ('service_type', models.CharField(max_length=50)),
                ('service_id', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
                ('payment_status', models.CharField(max_length=50)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Booking_Table',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overview', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image_gallery', models.JSONField()),
                ('reviews', models.TextField(blank=True, null=True)),
                ('hotels', models.JSONField()),
            ],
            options={
                'db_table': 'Package_Table',
            },
        ),
        migrations.CreateModel(
            name='DashboardItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('widget_type', models.CharField(max_length=50)),
                ('data_source', models.URLField(blank=True, null=True)),
                ('refresh_interval', models.IntegerField(default=0)),
                ('position', models.IntegerField(default=0)),
                ('settings', models.JSONField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Dashboard_Table',
            },
        ),
    ]
