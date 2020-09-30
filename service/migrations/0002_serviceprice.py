# Generated by Django 2.2 on 2020-09-27 07:55

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('draft', models.BooleanField(default=True)),
            ],
        ),
    ]