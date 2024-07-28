# Generated by Django 5.0.6 on 2024-07-23 12:38

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_html_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='html_text',
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=tinymce.models.HTMLField(null=True),
        ),
    ]