# Generated by Django 3.0.6 on 2020-06-23 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0025_auto_20200622_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glamember',
            name='rollno',
            field=models.IntegerField(help_text='university roll no', null=True),
        ),
    ]