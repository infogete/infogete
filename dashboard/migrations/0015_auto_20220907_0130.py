# Generated by Django 3.2.15 on 2022-09-07 01:30

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_article_article_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='message',
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=tinymce.models.HTMLField(default=None),
        ),
    ]
