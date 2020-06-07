# Generated by Django 3.0.6 on 2020-06-07 14:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(choices=[('btech', 'B.Tech'), ('mtech', 'M.Tech'), ('bphrama', 'B.Pharma'), ('mpharma', 'M.Pharma'), ('biotech', 'Biotech'), ('bba', 'BBA'), ('mba', 'MBA'), ('bca', 'BCA'), ('mca', 'MCA'), ('polytechnic', 'Polytechnic')], default='btech', max_length=50, unique=True)),
                ('duration', models.IntegerField(choices=[(1, '1 year'), (2, '2 years'), (3, '3 years'), (4, '4 years')], null=True)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='GLAMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=8, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999999'. Up to 12 digits allowed.", regex='^\\+?1?\\d{9,12}$')])),
                ('state', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('joined', models.DateField(blank=True, null=True)),
                ('working_days', models.IntegerField(blank=True, default=0, null=True)),
                ('photo', models.ImageField(null=True, upload_to=None)),
            ],
            options={
                'verbose_name': 'GLA Member',
                'verbose_name_plural': 'GLA Member',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'State',
                'verbose_name_plural': 'States',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=50, unique=True)),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.State')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=50)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Course')),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branches',
            },
        ),
    ]
