from django.urls import path
from . import views


urlpatterns = [
    path('single_students/<int:pk>', views.SingleStudent.as_view()),
    path('student_detail/<int:pk>', views.StudentDetail.as_view()),
    path('student_detail1/<int:no>', views.StudentDetail1.as_view()),
    path('student_detail2/<int:pk>', views.StudentDetail2.as_view()),
    path('student_detail3/<int:pk>', views.StudentDetail3.as_view()),
]
