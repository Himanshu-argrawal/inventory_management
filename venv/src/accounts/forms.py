from django import forms
from django.core.exceptions import ValidationError
from accounts.models import User

class Register_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Choose a password'
    }))
    class Meta:
        model = User
        fields = ['first_name' ,'username','last_name' ,'email']

        def clean_first_name(self):
            first_name = self.cleaned_data.get('first_name')
            if not re.match('^[a-zA-Z][a-zA-Z ]*$', first_name):
                raise forms.ValidationError(
                    'First name can only have alphabets and spaces')
            return first_name

        def clean_email(self):
            email = self.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Email already registered.')
            return email

        def clean_username(self):
            username = self.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError('Username already taken.')
            if not re.match('^[a-zA-Z][a-zA-Z0-9]*$', username):
                raise forms.ValidationError('Not valid username')
            return username

        def clean_password(self):
            password = self.cleaned_data.get('password')
            if(len(password)<=4):
                raise  forms.ValidationError("Mimnimum four characters required")
            if not re.match('[a-zA-Z][a-zA-Z0-9]*$',password):
                raise forms.ValidationError("Enter the alpha and numberic")
            return password

class Register_formTwo(forms.ModelForm):
    class Meta:
        model = User
        fields = ['gender','mobile','date_of_birth','country','state','address','pincode','company_name']

        def clean_username(self):
            username = self.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError('Username already taken.')
            if not re.match('^[a-zA-Z][a-zA-Z0-9]*$', username):
                raise forms.ValidationError('Not valid username')
            return username
        def clean_mobile(self):
            mobile = self.cleaned_data.get('mobile')
            if not re.match('^[1-9][0-9]{9}$', mobile):
                raise forms.ValidationError('Not a valid mobile number')
            return mobile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    remember = forms.BooleanField(required=False)

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if User.objects.filter(username = username ,password = password ).exists():
            pass
        else:
            raise ValidationError("Enter a correct email  or password ")




