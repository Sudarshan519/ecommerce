# Generated by Django 3.1.2 on 2020-11-01 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blogcomment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='thumbnail',
        ),
    ]
