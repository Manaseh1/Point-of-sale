from django import forms
from .models import Purchase
from inventory.models import Supplier

class order_form(forms.ModelForm):

    class Meta:
        model = Purchase
        fields = (
            'supplier',
        )
