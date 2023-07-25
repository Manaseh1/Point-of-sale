from django import forms
from .models import Purchase
from inventory.models import Supplier

class order_form(forms.ModelForm):
    order = forms.CharField(max_length = 100)
    class Meta:
        model = Purchase
        fields = (
            'supplier',
        )
