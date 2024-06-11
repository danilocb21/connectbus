from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth import get_user_model
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
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password1", "password2"]

class RegisterClientForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Nome'
    )
    last_name = forms.CharField(
        label="Sobrenome"
    )
    cpf = forms.CharField(
        label='CPF',
        max_length=11, 
    )
    primary_phone = forms.CharField(
        label='Telefone',
        max_length=11
    )
    optional_phone = forms.CharField(
        label='Telefone (Opcional)',
        max_length=11,
        required=False
    )
    birth_date = forms.DateField(
        label='Data de Nascimento'
    )
    street = forms.CharField(
        label='Rua',
        max_length=100
    )
    number = forms.CharField(
        label='Número',
        max_length=10
    )
    neighborhood = forms.CharField(
        label='Bairro',
        max_length=100
    )

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "birth_date", "cpf", "primary_phone", "optional_phone", "street", "number", "neighborhood"]

class RegisterCompanyForm(forms.ModelForm):
    name = forms.CharField(
        label='Nome',
    )
    cnpj = forms.CharField(
        label='CNPJ',
        max_length=14, 
    )
    phone = forms.CharField(
        label='Telefone',
        max_length=11
    )
    street = forms.CharField(
        label='Rua',
        max_length=100
    )
    number = forms.CharField(
        label='Número',
        max_length=10
    )

    class Meta:
        model = get_user_model()
        fields = ["name", "cnpj", "phone", "street", "number"]