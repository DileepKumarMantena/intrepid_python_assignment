from .models import *
from .serializers import *
from django.shortcuts import render, get_object_or_404,redirect
from .forms import *



def dashboard_items(request):
    items = DashboardItem.objects.all()
    return render(request, 'dashboard_items.html', {'items': items})

def bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings.html', {'bookings': bookings})

def packages(request):
    packages = Package.objects.all()
    return render(request, 'packages.html', {'packages': packages})

def edit_package(request, package_id):
    package = get_object_or_404(Package, pk=package_id)
    
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            # Update package details
            package.overview = form.cleaned_data['overview']
            package.cost = form.cleaned_data['cost']
            package.image_gallery = form.cleaned_data['image_gallery'].split(',')
            package.reviews = form.cleaned_data['reviews']
            package.hotels = form.cleaned_data['hotels'].split(',')
            package.save()
            return redirect('packages')
    else:
        # Prepopulate form with package details
        initial_data = {
            'overview': package.overview,
            'cost': package.cost,
            'image_gallery': ','.join(package.image_gallery),
            'reviews': package.reviews,
            'hotels': ','.join(package.hotels),
        }
        form = PackageForm(initial=initial_data)
    
    return render(request, 'edit_package.html', {'form': form, 'package': package})



def delete_package(request, package_id):
    package = get_object_or_404(Package, pk=package_id)
    
    if request.method == 'POST':
        # Confirm deletion
        package.delete()
        return redirect('packages')
    
    return render(request, 'delete_package.html', {'package': package})

def add_package(request):
    if request.method == 'POST':
        form = NewPackageForm(request.POST)
        if form.is_valid():
            # Create a new package instance and save
            new_package = Package(
                overview=form.cleaned_data['overview'],
                cost=form.cleaned_data['cost'],
                image_gallery=form.cleaned_data['image_gallery'].split(','),
                reviews=form.cleaned_data['reviews'],
                hotels=form.cleaned_data['hotels'].split(',')
            )
            new_package.save()
            return redirect('packages')
    else:
        form = NewPackageForm()
    
    return render(request, 'add_package.html', {'form': form})


