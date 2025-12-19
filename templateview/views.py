from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomeTemplateView(TemplateView):
    template_name = "core/home.html"


class ContextTemplateView(TemplateView):
    template_name = "core/context.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'jeka'
        return context


class NewsTemplateView(TemplateView):
    template_name = "core/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = 'Odooo has make jeka to ceo.'

        print(context)
        print(kwargs)

        return context
