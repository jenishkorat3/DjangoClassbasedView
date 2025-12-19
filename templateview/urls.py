from django.urls import path
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name="core/home.html"), name="main"),
    path('home/', views.TemplateView.as_view(template_name="core/home.html"), name="main"),
    path('home_view/', views.HomeTemplateView.as_view(), name="main"),
    path('context/', views.ContextTemplateView.as_view(), name="main"),
    path('extra_context/', views.ContextTemplateView.as_view(extra_context={'course':'computer'}), name="main"),
    path('news/<int:id>', views.NewsTemplateView.as_view(), name="main"),
]
