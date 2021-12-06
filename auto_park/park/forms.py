from django import forms
from django.conf import settings


class DriverFilterForm(forms.Form):
    created_at__lte = forms.DateField(required=False, input_formats=[settings.DATE_INPUT_FORMAT])
    created_at__gte = forms.DateField(required=False, input_formats=[settings.DATE_INPUT_FORMAT])

