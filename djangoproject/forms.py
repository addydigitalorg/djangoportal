from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignUpForm(UserCreationForm):

	class Meta:
	    fields = ('username','first_name','last_name','email','password1','password2')
	    model = User

	def __init__(self,*args,**kwargs):
	    super(SignUpForm, self).__init__(*args,**kwargs)
	    self.fields['password2'].label = 'Confirm Password (again)'
	    self.fields['email'].label = 'Email'

	    self.fields['username'].widget.attrs['class'] = 'form-control'
	    self.fields['first_name'].widget.attrs['class'] = 'form-control'
	    self.fields['last_name'].widget.attrs['class'] = 'form-control'
	    self.fields['email'].widget.attrs['class'] = 'form-control'
	    self.fields['password1'].widget.attrs['class'] = 'form-control'
	    self.fields['password2'].widget.attrs['class'] = 'form-control'


class LoginForm(AuthenticationForm):

	class Meta:
	    fields = ('username','password')

	def __init__(self,*args,**kwargs):
	    super(LoginForm, self).__init__(*args,**kwargs)

	    self.fields['username'].widget.attrs['class'] = 'form-control'
	    self.fields['password'].widget.attrs['class'] = 'form-control'