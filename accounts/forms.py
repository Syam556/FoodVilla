from django import forms

from .validators import allow_only_images_validator
from .models import User,UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': 'First Name'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'placeholder': 'Last Name'})
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Username'})
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': 'Email'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
        self.fields['confirm_password'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})

    
    def clean(self):
        cleaned_data=super(UserForm,self).clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')
        
        if password!=confirm_password:
            raise forms.ValidationError(
                "Password doesnot match!"
            )
        
class UserProfileForm(forms.ModelForm):
    address = forms.CharField(widget = forms.TextInput( attrs={'placeholder':'Start typing..','required':'required'}))
    profile_picture = forms.FileField(widget=forms.FileInput( attrs={'class': 'btn btn-info'}),validators =[allow_only_images_validator])
    cover_photo = forms.FileField(widget=forms.FileInput( attrs={'class': 'btn btn-info'}),validators =[allow_only_images_validator])
    
    latitude = forms.CharField(widget = forms.TextInput( attrs={'readonly':'readonly'}))
    longitude = forms.CharField(widget = forms.TextInput( attrs={'readonly':'readonly'}))
    class Meta:
        model = UserProfile
        fields = ['profile_picture','cover_photo','address','country','state','city','pin_code','latitude','longitude']



class UserInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number']