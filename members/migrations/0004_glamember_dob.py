# Generated by Django 3.0.6 on 2020-06-07 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20200607_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='glamember',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
