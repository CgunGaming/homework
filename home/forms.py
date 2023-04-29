from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import HomeWork


class NewUserForm(UserCreationForm):
    username = forms.CharField (
        label="username", 
        widget = forms.TextInput(attrs={
            "class": "form-control"
        }) 
    )
    password1 = forms.CharField( 
            label = "password", 
            widget=forms.PasswordInput(attrs={
                "class": "form-control"
            })
    )
    password2 = forms.CharField(
        label = "password",
        widget=forms.PasswordInput(attrs={
            "class": "form-control"
        })
    ) 
    
    
class LoginForm(AuthenticationForm):
    username = forms.CharField( 
        label="username",
        widget=forms.TextInput(attrs={
            "class": "form-control"  
        })
    )               
    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
        })
    )
    
    
class HomeWorkForm(forms.ModelForm):
    class Meta:
        model = HomeWork
        fields = ("title" , "content" , "deadline", "image", "lesson")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "deadline": forms.DateInput(attrs={"class": "form-control", "type":"date"}),
            "image": forms.ClearableFileInput(),
            "lesson": forms.Select(attrs={"class": "form-control"})
        }