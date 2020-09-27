from django.db import models
from fontawesome_5.fields import IconField
from ckeditor.fields import RichTextField

# Create your models here.
class ServiceItem(models.Model):
    icon = IconField(blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    details = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title


class ServicePrice(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    draft = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(blank=True, null=True , max_length=50)   

    def __str__(self):
        return self.name

class StrategicWork(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)   
    title = models.CharField(max_length=250, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to="work/image", blank=True, null=True)
    draft = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    