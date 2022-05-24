from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .bulma_mixin import BulmaMixin


class SignUpForm(BulmaMixin, UserCreationForm):
    username = forms.CharField(label='Write your username')
    email = forms.EmailField(label='Write your email')
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SignInFrom(BulmaMixin, AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'password']


class EditProfileForm(BulmaMixin, forms.ModelForm):
    email = forms.EmailField(label='Имя')
    phone = forms.CharField(label='Номер телефона')
    data_birthday = forms.DateField(label='Data birthday')
    phone2 = forms.CharField(label='Номер телефона')
    pin = forms.CharField(label='Введите четыре цифры (Pin)')

    class Meta:
        model = User
        fields = ['email', 'phone', 'data_birthday', 'phone2', 'pin']


class ChangePasswordForm(BulmaMixin, PasswordChangeForm):
    old_password = forms.PasswordInput()
    new_password1 = forms.PasswordInput()
    new_password2 = forms.PasswordInput()


class Meta:
    model = User
    fields = ['old_password', 'new_password1', 'new_password2']
