from django.shortcuts import render
from django.views.generic import TemplateView
from service.models import ServiceItem, ServicePrice, StrategicWork
# Create your views here.


class IndexTemplateView(TemplateView):
    template_name = "index.html"

class AboutTemplateView(TemplateView):
    template_name = "about.html"

class ServiceTemplateView(TemplateView):
    template_name = "services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service"] = ServiceItem.objects.all()
        context["service_price"] = ServicePrice.objects.all()
        context["strategic_work"] = StrategicWork.objects.all()
        return context
    

class CasesTemplateView(TemplateView):
    template_name = "cases.html"

class BlogTemplateView(TemplateView):
    template_name = "blog.html"

class ContactTemplateView(TemplateView):
    template_name = "contact.html"