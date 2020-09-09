from django.urls import path
from .views import IndexTemplateView, AboutTemplateView, ServiceTemplateView, CasesTemplateView, BlogTemplateView, ContactTemplateView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name="index"),
    path('about', AboutTemplateView.as_view(), name="about"),
    path('service', ServiceTemplateView.as_view(), name="service"),
    path('cases', CasesTemplateView.as_view(), name="cases"),
    path('blog', BlogTemplateView.as_view(), name="blog"),
    path('contact', ContactTemplateView.as_view(), name="contact"),
]
