from django.shortcuts import render
from .forms import ContactForm, StudentForm
from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.contrib import messages
from .models import Student


class ContactFormView(FormView):
    template_name = 'formview/contact.html'
    form_class = ContactForm

    success_url = '/form/thanks/'

    initial = {'name': 'jenish'}
    def form_valid(self, form):
        print(form.cleaned_data['name'])
        print(form.cleaned_data['desc'])
        return super().form_valid(form)
        # return HttpResponse("Thank You")

    def form_invalid(self, form):
        messages.error(self.request, "Not Possible")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["extra"] = "Form view"
        return context


class StudentFormView(FormView):
    template_name = 'formview/student.html'
    form_class = StudentForm
    success_url = '/form/thanks/'

    def form_valid(self, form):
        roll = form.cleaned_data['roll']
        name = form.cleaned_data['name']
        course = form.cleaned_data['course']

        student = Student(roll=roll, name=name, course=course)
        student.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Not Possible")
        return super().form_invalid(form)
