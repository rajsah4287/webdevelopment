from django import forms
from dashboard.models import Staff

class StaffForm(forms.ModelForm):
    class Meta:
        model=Staff
        fields="__all__"