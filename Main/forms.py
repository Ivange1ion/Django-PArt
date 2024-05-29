from django import forms
class UserForm(forms.Form):
    nickname=forms.CharField(max_length=25)
    age=forms.DateField()
    mail=forms.EmailField()
    password=forms.CharField(max_length=25, widget=forms.PasswordInput)
    age=forms.DateField()

class AuthForm(forms.Form):
    mail=forms.EmailField()
    password=forms.CharField( widget=forms.PasswordInput)

class AddForm(forms.Form):
    artname=forms.CharField(max_length=25)
    art=forms.FileField()
    tag1=forms.CharField(max_length=25)
    tag2=forms.CharField(max_length=25)
    tag3=forms.CharField(max_length=25)
    tag4=forms.CharField(max_length=25)
    tag5=forms.CharField(max_length=25)
    author=forms.CharField()