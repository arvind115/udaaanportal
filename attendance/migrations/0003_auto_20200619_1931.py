# Generated by Django 3.0.6 on 2020-06-19 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20200619_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]