from django import forms

from .models import UserResult
from .models import Answer


class UserResultForm(forms.ModelForm):
    class Meta:
        model = UserResult
        fields = ['name', 'gender', 'age']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['order']

