from django import forms
from .models import Product,Supplier, Category

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'product_type': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'date_added': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'units': forms.TextInput(attrs={'class': 'form-control'}),
            'supplier_name': forms.HiddenInput(attrs={'class': 'form-control'}),
        }

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ('name', 'email', 'address', 'phone_number')
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description', 'parent')