from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"placeholder": "Имя пользователя"})
        self.fields["password"].widget.attrs.update({"placeholder": "Пароль"})



class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Электронная почта'}))
    password1 = forms.CharField(label='Password', strip=False, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Password confirm', strip=False, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    ENGLISH_LEVEL_CHOICES = (
        ('A1', 'Beginner'),
        ('A2', 'Elementary'),
        ('B1', 'Intermediate'),
        ('B2', 'Upper Intermediate'),
        ('C1', 'Advanced'),
        ('C2', 'Proficiency'),
    )
    english_level = forms.ChoiceField(choices=ENGLISH_LEVEL_CHOICES, initial='A1')

    class Meta:
        model = User
        fields = ['username', 'email', 'english_level', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Этот email уже занят.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.english_level = self.cleaned_data['english_level']
        if commit:
            user.save()
        return user


