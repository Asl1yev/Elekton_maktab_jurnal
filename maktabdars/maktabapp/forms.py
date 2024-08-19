from django import forms
from .models import Student,Fan,Baholar



class AddFanForm(forms.ModelForm):
    class Meta:
        model=Fan
        fields=['name']

class AddStudntForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['ismi','familyasi','fan_nomi']


class AddBahoForm(forms.ModelForm):
    class Meta:
        model=Baholar
        fields=['fan','talaba','baho']