from django import forms
from .models import Register
from .models import Contact_Us

class RegisterForm(forms.ModelForm):
    
    class Meta:
    	model = Register
    	fields = ('full_name', 'email',)


class Contact_UsForm(forms.ModelForm):
    
    class Meta:
    	model = Contact_Us
    	fields = ('full_name', 'email', 'phone', 'question')