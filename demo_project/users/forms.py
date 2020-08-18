from .models import Signup, Blog
from django import forms
from django.forms import ModelForm

class Signupform(ModelForm):
    username = forms.CharField(widget=forms.TextInput)
    email_address = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Signup
        fields = "__all__"


    def clean_username(self):
        myusername = self.cleaned_data.get('username')
        check_if_user_exists = Signup.objects.filter(username=myusername).exists()
        if check_if_user_exists:
            raise forms.ValidationError("Oops, looks like the username already exists!")
        return myusername

    def clean_email_address(self):
        myemail = self.cleaned_data.get('email_address')
        check_if_email_exists = Signup.objects.filter(email_address=myemail).exists()
        if check_if_email_exists:
            raise forms.ValidationError("Oops, this email address is already registered with a user. Please enter a different email address")
        return myemail

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password and Confirm Password mismatch")
        return confirm_password



class Loginform(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    email_address = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        myusername = self.cleaned_data.get('username')
        check_if_user_exists = Signup.objects.filter(username = myusername).exists()
        if check_if_user_exists:
            pass
        else:
            raise forms.ValidationError("Please enter a valid username. If you haven't signed up, please visit sign up page")
        return myusername

    def clean_email_address(self):
        myemail = self.cleaned_data.get('email_address')
        check_if_email_exists = Signup.objects.filter(email_address = myemail).exists()
        if check_if_email_exists:
            pass
        else:
            raise forms.ValidationError("Please enter a valid email address. If you haven't signed up, please visit sign up page")
        return myemail

    def clean_password(self):
        mypass = self.cleaned_data.get('password')
        check_if_pass_exists = Signup.objects.filter(password = mypass).exists()
        if check_if_pass_exists:
            pass
        else:
            raise forms.ValidationError("Wrong password. If you haven't signed up, please visit sign up page")
        return mypass


class Createblogfrom(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Blog
        fields = "__all__"