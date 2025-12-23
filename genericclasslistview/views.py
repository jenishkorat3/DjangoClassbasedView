from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from .models import Student


class AllStudent(View):
    def get(self ,request):
        all_students = Student.objects.all()
        return render(request, 'genericclasslistview/all_student.html', {'all_students': all_students})


class StudentList(ListView):
    #default template_name = student_list
    #default context_name = student_list
    model = Student


class StudentList1(ListView):
    model = Student
    template_name_suffix = '_all'
    ordering = ['name']


class StudentList2(ListView):
    model = Student
    template_name = 'genericclasslistview/all_student.html'
    context_object_name = 'all_students'


class StudentList3(ListView):
    model = Student
    template_name = 'genericclasslistview/all_student.html'
    context_object_name = 'all_students'

    def get_queryset(self):
        return Student.objects.filter(course = 'Python')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teacher"] = 'jeka'
        return context

    def get_template_names(self) -> list[str]:
        if self.request.COOKIES.get('user') == 'sonam':
            return ["genericclasslistview/student_list.html"]
        return super().get_template_names()

