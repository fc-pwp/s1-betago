from django import forms

from .models import UserResult


class UserResultForm(forms.ModelForm):
    class Meta:
        model = UserResult
        fields = ['name', 'gender', 'age']

