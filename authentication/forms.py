from django.forms import ModelForm, Form, CharField
from .models import User

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

class LoginForm(Form):
    class Meta():
        model = User
        fields = ['email' , 'password']


