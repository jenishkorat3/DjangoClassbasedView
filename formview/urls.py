from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('contact/', views.ContactFormView.as_view()),
    path('thanks/', TemplateView.as_view(template_name = 'formview/thanks.html')),
    path('student/', views.StudentFormView.as_view()),
]
