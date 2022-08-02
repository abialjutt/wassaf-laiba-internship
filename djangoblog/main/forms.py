from enum import unique
from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required= True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    age = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "age", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.age = self.cleaned_data["age"]
        if commit:
            user.save()
        return user
