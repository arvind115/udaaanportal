# Generated by Django 3.0.6 on 2020-06-08 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0010_auto_20200608_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='glamember',
            name='preferred_days',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=15, null=True),
        ),
    ]