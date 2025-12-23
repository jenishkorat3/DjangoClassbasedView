from django import forms
from .models import Student


class ContactForm(forms.Form):
    name = forms.CharField()
    desc = forms.CharField(widget=forms.Textarea)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
