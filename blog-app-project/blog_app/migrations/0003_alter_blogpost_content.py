# Generated by Django 5.1.2 on 2024-11-04 07:45

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_blogpost_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
    ]
