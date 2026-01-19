from django import forms
from .models import Staff_Member

class StaffMemberForm(forms.ModelForm): # Use ModelForm here
    class Meta:
        model = Staff_Member
        fields = '__all__'

