# Generated by Django 3.0.6 on 2020-06-21 07:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import members.models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0022_auto_20200620_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glamember',
            name='branch',
            field=models.ForeignKey(help_text='select Branch', null=True, on_delete=django.db.models.deletion.CASCADE, to='members.Branch'),
        ),
        migrations.AlterField(
            model_name='glamember',
            name='city',
            field=models.ForeignKey(help_text='select city', null=True, on_delete=django.db.models.deletion.CASCADE, to='members.City'),
        ),
        migrations.AlterField(
            model_name='glamember',
            name='course',
            field=models.ForeignKey(help_text='select course', null=True, on_delete=django.db.models.deletion.CASCADE, to='members.Course'),
        ),
        migrations.AlterField(
            model_name='glamember',
            name='dob',
            field=models.DateField(help_text='DOB: mm-dd-yyyy', null=True),
        ),
        migrations.AlterField(
            model_name='glamember',
            name='email',
            field=models.EmailField(help_text='your GLA email id', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='glamember',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], help_text='select your gender', max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='glamember',
            name='joined_in',
            field=models.DateField(blank=True, help_text='date of joining Udaaan', null=True),
        ),
        migrations.AlterField(
            model_name='glamember',
            name='name',
            field=models.CharField(help_text='your full name', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='glamember',
            name='phone',
            field=models.CharField(blank=True, help_text='+91xxxxxxxxxx', max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: +91xxxxxxxxxx', regex='^\\+?1?\\d{9,10}$')]),
        ),
        migrations.AlterField(
            model_name='glamember',
            name='photo',
            field=models.ImageField(help_text='your profile photo', null=True, upload_to=members.models.store_file_name),
        ),
        migrations.AlterField(
            model_name='glamember',
            name='preferred_days',
            field=models.ManyToManyField(help_text='select days you want to work on', to='members.Day'),
        ),
        migrations.AlterField(
            model_name='glamember',
            name='rollno',
            field=models.IntegerField(blank=True, help_text='university roll no', null=True),
        ),
        migrations.AlterField(
            model_name='glamember',
            name='state',
            field=models.ForeignKey(help_text='select state', null=True, on_delete=django.db.models.deletion.CASCADE, to='members.State'),
        ),
        migrations.AlterField(
            model_name='glamember',
            name='username',
            field=models.CharField(help_text='your username,non-editable', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='glamember',
            name='working_days',
            field=models.IntegerField(blank=True, default=0, help_text='non-editable', null=True),
        ),
        migrations.AlterField(
            model_name='glamember',
            name='year',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], help_text='select year', null=True),
        ),
    ]
