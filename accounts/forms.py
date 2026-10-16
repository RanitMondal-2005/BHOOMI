# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

# this form is for the register page
# UserCreationForm builtin Form, it handles - username, password, password confirmation and validation
# we are just adding the email field to it since django's default form does not include email
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['username'].widget.attrs.update({
                'placeholder': 'Choose a username',
            })
            self.fields['email'].widget.attrs.update({
                'placeholder': 'you@example.com',
            })
            self.fields['password1'].widget.attrs.update({
                'placeholder': 'Enter password',
            })
            self.fields['password2'].widget.attrs.update({
                'placeholder': 'Re-enter password',
            })

class StyledLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter your username',
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Enter your password',
        })
