from attr import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import todo
class signpageform(UserCreationForm):
    password2 = forms.CharField(label='password(again)',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        label = {'email':'Email'}


class todoform(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['title','status','priority']