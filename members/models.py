from django.db import models
from django.db.models.signals import post_save
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.urls import reverse
from os import path,remove
from django.conf import settings

# Create your models here.
class State(models.Model):
  state = models.CharField(null=True,blank=True,max_length=50)

  def __str__(self):
    return self.state
  
  class Meta:
    verbose_name = 'State'
    verbose_name_plural = 'States'

class City(models.Model):
  city  = models.CharField(max_length=50,blank=True,unique=True)
  state = models.ForeignKey(State,null=True,blank=True, on_delete=models.CASCADE)

  def __str__(self):
    return self.city

  class Meta:
    verbose_name = 'City'
    verbose_name_plural = 'Cities'

class Course(models.Model):
  course_choices = (
    ('B.Tech','B.Tech'),
    ('M.Tech','M.Tech'),
    ('bphrama','B.Pharma'),
    ('mpharma','M.Pharma'),
    ('biotech','Biotech'),
    ('bba','BBA'),
    ('mba','MBA'),
    ('bca','BCA'),
    ('mca','MCA'),
    ('polytechnic','Polytechnic')
  )
  duration_choices = (
    (1,'1 year'),
    (2,'2 years'),
    (3,'3 years'),
    (4,'4 years')
  )
  course =  models.CharField(
                max_length=50,
                choices=course_choices,
                default='btech',
                blank=False,
                unique=True)
  duration = models.IntegerField(null=True,choices=duration_choices)

  class Meta:
    verbose_name = 'Course'
    verbose_name_plural = 'Courses'

  def __str__(self):
      return self.course

class Branch(models.Model):
  branch = models.CharField(
           max_length=50,
           blank=False,
           unique=False)
  course = models.ForeignKey(Course, on_delete=models.CASCADE)

  def __str__(self):
      return self.branch
  
  class Meta:
    verbose_name = 'Branch'
    verbose_name_plural = 'Branches'

class Day(models.Model):
  DAYS_CHOICES = (
    ('Monday','Monday'),
    ('Tuesday','Tuesday'),
    ('Wednesday','Wednesday'),
    ('Thursday','Thursday'),
    ('Friday','Friday'),
    ('Saturday','Saturday'),
    ('Sunday','Sunday'),
  )
  day = models.CharField(max_length=15,null=True,choices=DAYS_CHOICES)

  def __str__(self):
    return self.day
  
  class Meta:
    verbose_name = 'Day'
    verbose_name_plural = 'Days'


def store_file_name(instance,filename):
  ext = path.splitext(filename)[1]
  FILE_PATH = path.join(settings.MEDIA_ROOT,'avatars',f'{instance.username}{ext}')
  if path.isfile(FILE_PATH):
    remove(FILE_PATH)
  return f'avatars/{instance.username}{ext}'
  
class GLAMember(models.Model):
  gender_choices = (
    ("",""),
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')
  )

  user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
  username  = models.CharField(max_length=50,null=True,help_text='your username,non-editable')
  name      = models.CharField(max_length=50,null=True,help_text='your full name')
  gender    = models.CharField(max_length=8,choices=gender_choices,null=True,help_text='select your gender')
  dob       = models.DateField(null=True,auto_now=False, auto_now_add=False,help_text='DOB: mm-dd-yyyy')
  email     = models.EmailField(max_length=50,null=True,help_text='your GLA email id')
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,13}$', 
            message="Phone number must be entered in the format: +91xxxxxxxxxx")
  phone = models.CharField(validators=[phone_regex], max_length=13, blank=True,help_text='+91xxxxxxxxxx') # validators should be a list
  state = models.ForeignKey(State,null=True, on_delete=models.CASCADE,help_text='select state')
  city = models.ForeignKey(City,null=True, on_delete=models.CASCADE,help_text='select city')
  course = models.ForeignKey(Course,null=True, on_delete=models.CASCADE, help_text='select course')
  branch  = models.ForeignKey(Branch,null=True, on_delete=models.CASCADE,help_text='select Branch')
  year = models.IntegerField(null=True,choices=(("",""),(1,1),(2,2),(3,3),(4,4)),help_text='select year')
  rollno = models.IntegerField(null=True,blank=True,help_text='university roll no')
  joined_in = models.DateField(blank=True,null=True,auto_now=False, auto_now_add=False,help_text='date of joining Udaaan')
  working_days = models.IntegerField(default=0,null=True,blank=True,help_text='non-editable')
  preferred_days = models.ManyToManyField(Day,help_text='select days you want to work on')
  photo = models.ImageField(upload_to=store_file_name,null=True,help_text='your profile photo')

  def __str__(self):
    return self.username

  def get_absolute_url(self):
      return reverse('memberdetails', kwargs={'slug': self.username})
  
  class Meta:
    verbose_name = 'GLA Member'
    verbose_name_plural = 'GLA Members'
