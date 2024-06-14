# forms.py
from django import forms

class PackageForm(forms.Form):
    overview = forms.CharField(label='Overview', max_length=255)
    cost = forms.DecimalField(label='Cost', max_digits=10, decimal_places=2)
    image_gallery = forms.CharField(label='Image Gallery', widget=forms.Textarea)
    reviews = forms.CharField(label='Reviews', widget=forms.Textarea)
    hotels = forms.CharField(label='Hotels', widget=forms.Textarea)


class NewPackageForm(forms.Form):
    overview = forms.CharField(label='Overview', max_length=255)
    cost = forms.DecimalField(label='Cost', max_digits=10, decimal_places=2)
    image_gallery = forms.CharField(label='Image Gallery', widget=forms.Textarea)
    reviews = forms.CharField(label='Reviews', widget=forms.Textarea)
    hotels = forms.CharField(label='Hotels', widget=forms.Textarea)
