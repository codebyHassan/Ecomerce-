from django import forms
from django.contrib.auth.forms import PasswordResetForm , AuthenticationForm
from django.contrib.auth.models import User

# class CustomerRegisterationForm(UserCreationForm):
#     password1 = forms.CharField(label='password' , widget=forms.PasswordInput(attrs={
#         'class':'form-control'
#     }))
#     password1 = forms.CharField(label='Confirm password(Again)' , widget=forms.PasswordInput(attrs={
#         'class':'form-control'
#     }))

#     email = forms.CharField(label='Email' , required=True , widget=forms.EmailInput(attrs={
#         'class':'form-control'
#     }))

#     class Meta:
#         model = User 
#         fields = ['username', 'email','password1','password2']
#         labels = {'email':'Email'}
#         widgets = {'username': forms.Textarea(attrs={
#             'class':'form-control'
#         })}



class myPasswordResetFrom(PasswordResetForm):
    email = forms.EmailField(label=("Email") , max_length=256 , widget=forms.EmailInput(attrs={'autocomplete':'email', 'class':'form-control'}))