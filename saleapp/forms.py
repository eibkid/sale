
from dataclasses import fields
from random import choices
from django import forms

from .models import Extract



class ExtractForm(forms.ModelForm):
    class Meta:
        model = Extract
        fields = ('Sales_person', 'Customer_name','customer_country', 'Desired_fruit')

