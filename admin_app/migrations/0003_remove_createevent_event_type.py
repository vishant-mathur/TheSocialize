# Generated by Django 4.0.5 on 2023-03-18 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0002_createevent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createevent',
            name='event_type',
        ),
    ]