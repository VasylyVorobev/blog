from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Придумайте пароль', min_length=5)
    password1 = forms.CharField(widget=forms.PasswordInput, label='Введите пароль еще раз', min_length=5)
    username = forms.CharField(label='Логин')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с ником "{username}" уже существует.')
        return username

    def clean_password1(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password1']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password1']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'Данная почта уже используется')
        return email
