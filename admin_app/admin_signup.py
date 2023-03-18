from django import forms  
from admin_app.models import Admin_signup  
  
class Adminsignup(forms.ModelForm):  
    class Meta:  
        model = Admin_signup  
        fields = "__all__"  
        widgets={
            'Name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password' : forms.TextInput(attrs={'class':'form-control'})
        }