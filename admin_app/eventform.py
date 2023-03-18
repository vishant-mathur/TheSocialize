from django import forms  
from admin_app.models import CreateEvent  
class EventForm(forms.ModelForm):  
    class Meta:  
        model = CreateEvent  
        fields = "__all__"