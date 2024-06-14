from rest_framework import serializers
from .models import *

class DashboardItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashboardItem
        fields = ['id', 'title', 'description', 'widget_type', 'data_source', 'refresh_interval', 'position', 'settings']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'customer_name', 'customer_email', 'customer_phone', 'booking_date', 'service_type', 'service_id', 'status', 'payment_status', 'notes']

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['id', 'overview', 'cost', 'image_gallery', 'reviews', 'hotels']
