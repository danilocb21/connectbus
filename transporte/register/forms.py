from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django import forms

class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Usuário',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label='Senha',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    username = UsernameField(
        label='Usuário',
        widget=forms.TextInput(attrs={'autofocus': True}),
        help_text="Necessário. 150 caracteres ou menos. Letras, dígitos e @/./+/-/_ apenas."
    )
    password1 = forms.CharField(
        label='Senha',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
        help_text="""
        <ul>
            <li>Sua senha não pode ser muito parecida com suas outras informações pessoais.</li>
            <li>Sua senha precisa conter pelo menos 8 caracteres.</li>
            <li>Sua senha não pode ser uma senha comumente utilizada.</li>
            <li>Sua senha não pode ser inteiramente numérica.</li>
        </ul>
    """
    )
    password2 = forms.CharField(
        label='Confirme sua senha',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
        help_text="Digite a mesma senha novamente, para verificação."
    )


    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        