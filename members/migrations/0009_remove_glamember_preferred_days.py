# Generated by Django 3.0.6 on 2020-06-07 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_auto_20200607_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='glamember',
            name='preferred_days',
        ),
    ]
