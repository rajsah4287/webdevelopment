from django import forms
from order.models import OrderConfirmed

class OrderForm(forms.ModelForm):
    class Meta:
        model=OrderConfirmed
        fields="__all__"