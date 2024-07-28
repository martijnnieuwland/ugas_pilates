# Generated by Django 5.0.6 on 2024-07-23 13:09

import datetime
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_html_text_alter_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lead',
            field=models.TextField(default=datetime.datetime(2024, 7, 23, 13, 8, 56, 744741, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=tinymce.models.HTMLField(default=datetime.datetime(2024, 7, 23, 13, 9, 55, 363802, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]