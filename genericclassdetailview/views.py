from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.detail import DetailView
from .models import Student


class SingleStudent(View):
    def get(self ,request, pk):
        all_students = Student.objects.filter(pk=pk)
        return render(request, 'genericclassdetailview/all_student.html', {'all_students': all_students})


class StudentDetail(DetailView):
    #default template_name = student_detail
    #default context_name = student_detail
    #default <int:pk> = pk or slug
    model = Student


class StudentDetail1(DetailView):
    model = Student
    pk_url_kwarg = 'no'
    template_name_suffix = '_one'
    ordering = ['name']


class StudentDetail2(DetailView):
    model = Student
    template_name = 'genericclassdetailview/student_stu.html'
    context_object_name = 'stu'


class StudentDetail3(DetailView):
    model = Student
    template_name = 'genericclassdetailview/student_stu.html'
    context_object_name = 'stu'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teacher"] = 'jeka'
        return context
