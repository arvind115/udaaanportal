# Generated by Django 3.0.6 on 2020-06-12 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_auto_20200610_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
