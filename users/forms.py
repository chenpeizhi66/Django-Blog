from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

# official intro to form: https://docs.djangoproject.com/en/3.2/topics/forms/

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=32, widget=forms.TextInput(attrs={
        'class': 'input', 'placeholder': 'Username/Email'
    }))
    password = forms.CharField(label='Password', min_length=6, widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder':'Password'
    }))
    
    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if username == password:
            raise forms.ValidationError('password can not be the same to username')
        return password

class RegisterForm(forms.ModelForm):
    '''
    Using ModelForm that can create a Form class from User
    P.S: Django already has the function to check duplicate username, no need to write by ourselves
    '''
    username = forms.CharField(label='Username', max_length=32, widget=forms.TextInput(attrs={
        'class': 'input', 'placeholder': 'Username/Email'
    }))
    password = forms.CharField(label='Password', min_length=6, widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder':'Password'
    })) # hide password when we input it
    
    password_repeat = forms.CharField(label='Repeat Your Password', min_length=6, widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder':'Password'
    })) # hide password when we input it
    
    class Meta:
        model = User
        fields = ('username', 'password')

    def clean_password_repeat(self):
        if self.cleaned_data['password'] != self.cleaned_data['password_repeat']:
            raise forms.ValidationError('Password mismatch!')
        return self.cleaned_data['password_repeat']

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('email',)


class UserProfileForm(forms.ModelForm):
    """Form definition for UserInfo."""
 
    class Meta:
        """Meta definition for UserInfoform."""

        model = UserProfile
        fields = ('nickname','desc', 'birthday',  'gender', 'address', 'image')
