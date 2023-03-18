from social.models import User_signup
from django import forms  


class Usersignup(forms.ModelForm):  
    class Meta:  
        model = User_signup  
        fields = "__all__"  
        widgets={
            'Name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password' : forms.TextInput(attrs={'class':'form-control'})
        }