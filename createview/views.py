from django.shortcuts import render
from .forms import  StudentForm
from django.views.generic.edit import CreateView, UpdateView
from .models import Student
from django import forms


#create view
class StudentCreateView(CreateView):
    model = Student
    fields = ['roll', 'name', 'course']
    # success_url = '/create/thanks/'
    template_name = 'createview/register.html'

    def get_form(self):
        form = super().get_form()

        form.fields['name'].widget = forms.TextInput(attrs={'class': 'myclass'})
        form.fields['course'].widget = forms.Textarea()

        return form


class StudentCreateView1(CreateView):
    form_class = StudentForm
    template_name = 'createview/register.html'



# Update view
class StudentUpdateView(UpdateView):
    model = Student
    fields = ['roll', 'name', 'course']


class StudentUpdateView1(UpdateView):
    model = Student
    fields = ['roll', 'name', 'course']
    template_name = 'createview/register.html'

    def get_form(self):
        form = super().get_form()

        form.fields['name'].widget = forms.TextInput(attrs={'class': 'myclass'})
        form.fields['course'].widget = forms.Textarea()

        return form


class StudentUpdateView2(UpdateView):
    model = Student
    form_class = StudentForm
