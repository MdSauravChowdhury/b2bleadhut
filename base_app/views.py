from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class IndexTemplateView(TemplateView):
    template_name = "index.html"

class AboutTemplateView(TemplateView):
    template_name = "about.html"

class ServiceTemplateView(TemplateView):
    template_name = "services.html"

class CasesTemplateView(TemplateView):
    template_name = "cases.html"

class BlogTemplateView(TemplateView):
    template_name = "blog.html"

class ContactTemplateView(TemplateView):
    template_name = "contact.html"