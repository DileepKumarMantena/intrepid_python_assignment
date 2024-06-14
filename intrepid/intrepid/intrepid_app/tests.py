from django.test import TestCase, Client
from django.urls import reverse
from .models import DashboardItem, Booking, Package

class DashboardItemsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('dashboard_items')

    def test_dashboard_items_view(self):
        # Create test data
        DashboardItem.objects.create(name='Item 1', description='Description 1')
        DashboardItem.objects.create(name='Item 2', description='Description 2')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard_items.html')
        self.assertContains(response, 'Item 1')
        self.assertContains(response, 'Item 2')

class BookingsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('bookings')

    def test_bookings_view(self):
        # Create test data
        Booking.objects.create(name='Booking 1', details='Details 1')
        Booking.objects.create(name='Booking 2', details='Details 2')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings.html')
        self.assertContains(response, 'Booking 1')
        self.assertContains(response, 'Booking 2')

class PackagesViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('packages')

    def test_packages_view(self):
        # Create test data
        Package.objects.create(overview='Package 1', cost=100.0)
        Package.objects.create(overview='Package 2', cost=200.0)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'packages.html')
        self.assertContains(response, 'Package 1')
        self.assertContains(response, 'Package 2')

class EditPackageViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.package = Package.objects.create(
            overview='Test Package', cost=100.0, image_gallery=['img1', 'img2'],
            reviews='Good', hotels=['Hotel1', 'Hotel2']
        )
        self.url = reverse('edit_package', args=[self.package.id])

    def test_edit_package_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_package.html')
        self.assertContains(response, 'Test Package')

    def test_edit_package_view_post(self):
        data = {
            'overview': 'Updated Package',
            'cost': 150.0,
            'image_gallery': 'img1,img2,img3',
            'reviews': 'Excellent',
            'hotels': 'Hotel1,Hotel2,Hotel3'
        }
        response = self.client.post(self.url, data)
        self.assertRedirects(response, reverse('packages'))
        self.package.refresh_from_db()
        self.assertEqual(self.package.overview, 'Updated Package')
        self.assertEqual(self.package.cost, 150.0)
        self.assertEqual(self.package.image_gallery, ['img1', 'img2', 'img3'])
        self.assertEqual(self.package.reviews, 'Excellent')
        self.assertEqual(self.package.hotels, ['Hotel1', 'Hotel2', 'Hotel3'])

class DeletePackageViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.package = Package.objects.create(overview='Test Package', cost=100.0)
        self.url = reverse('delete_package', args=[self.package.id])

    def test_delete_package_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_package.html')
        self.assertContains(response, 'Test Package')

    def test_delete_package_view_post(self):
        response = self.client.post(self.url)
        self.assertRedirects(response, reverse('packages'))
        with self.assertRaises(Package.DoesNotExist):
            self.package.refresh_from_db()

class AddPackageViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('add_package')

    def test_add_package_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_package.html')

    def test_add_package_view_post(self):
        data = {
            'overview': 'New Package',
            'cost': 120.0,
            'image_gallery': 'img1,img2',
            'reviews': 'Good',
            'hotels': 'Hotel1,Hotel2'
        }
        response = self.client.post(self.url, data)
        self.assertRedirects(response, reverse('packages'))
        new_package = Package.objects.get(overview='New Package')
        self.assertEqual(new_package.cost, 120.0)
        self.assertEqual(new_package.image_gallery, ['img1', 'img2'])
        self.assertEqual(new_package.reviews, 'Good')
        self.assertEqual(new_package.hotels, ['Hotel1', 'Hotel2'])
