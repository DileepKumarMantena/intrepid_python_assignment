from django.db import models
from django.contrib.auth.models import User

class DashboardItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    widget_type = models.CharField(max_length=50)
    data_source = models.URLField(blank=True, null=True)
    refresh_interval = models.IntegerField(default=0)
    position = models.IntegerField(default=0)
    settings = models.JSONField(blank=True, null=True)

    class Meta:
        db_table = "Dashboard_Table"

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15, blank=True, null=True)
    booking_date = models.DateTimeField()
    service_type = models.CharField(max_length=50)
    service_id = models.IntegerField()
    status = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "Booking_Table"


class Package(models.Model):
    overview = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    image_gallery = models.JSONField()
    reviews = models.TextField(blank=True, null=True)
    hotels = models.JSONField()

    class Meta:
        db_table = "Package_Table"
