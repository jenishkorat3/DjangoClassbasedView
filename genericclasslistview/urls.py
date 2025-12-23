from django.urls import path
from . import views


urlpatterns = [
    path('all_students/', views.AllStudent.as_view()),
    path('student_list/', views.StudentList.as_view()),
    path('student_list1/', views.StudentList1.as_view()),
    path('student_list2/', views.StudentList2.as_view()),
    path('student_list3/', views.StudentList3.as_view()),
]
