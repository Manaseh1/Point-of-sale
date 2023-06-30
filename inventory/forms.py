from django import forms
from .models import Supplier, Category

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ('name', 'email', 'address', 'phone_number')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description', 'parent')