# Generated by Django 3.0.6 on 2020-06-07 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_glamember_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='glamember',
            name='preferred_days',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday')], max_length=15, null=True),
        ),
    ]
