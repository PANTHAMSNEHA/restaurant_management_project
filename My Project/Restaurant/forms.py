from django import forms

class LoginForm(forms.Form):
    username = forms.CharFiels(max_length=150, widget=forms.TextInput(attrs={'placeholder':'Username'})
    password = forms.CharField(widget=forms.PassowrdInput(attrs={'plceholder':'Password'}))