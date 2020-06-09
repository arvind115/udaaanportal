from django.db import models
from django.db.models.signals import post_save
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.urls import reverse

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
    ('btech','B.Tech'),
    ('mtech','M.Tech'),
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
  return 'avatars/{0}.{1}'.format(instance.username,filename.split('.')[-1])

class GLAMember(models.Model):
  gender_choices = (
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')
  )

  user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
  username  = models.CharField(max_length=50,null=True)
  name      = models.CharField(max_length=50,null=True)
  gender    = models.CharField(max_length=8,choices=gender_choices,null=True)
  dob       = models.DateField(null=True,auto_now=False, auto_now_add=False)
  email     = models.EmailField(max_length=50,null=True)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', 
            message="Phone number must be entered in the format: +91xxxxxxxxxx")
  phone = models.CharField(validators=[phone_regex], max_length=10, blank=True) # validators should be a list
  state = models.ForeignKey(State,null=True, on_delete=models.CASCADE)
  city = models.ForeignKey(City,null=True, on_delete=models.CASCADE)
  course = models.ForeignKey(Course,null=True, on_delete=models.CASCADE)
  branch  = models.ForeignKey(Branch,null=True, on_delete=models.CASCADE)
  year = models.IntegerField(null=True,choices=((1,1),(2,2),(3,3),(4,4)))
  rollno = models.IntegerField(null=True,default=0)
  joined_in = models.DateField(blank=True,null=True,auto_now=False, auto_now_add=False)
  working_days = models.IntegerField(default=0,null=True,blank=True)
  preferred_days = models.ManyToManyField(Day)
  photo = models.FileField(upload_to=store_file_name,null=True)

  def __str__(self):
    return self.username

  def get_absolute_url(self):
      return reverse('memberdetails', kwargs={'slug': self.username})
  
  class Meta:
    verbose_name = 'GLA Member'
    verbose_name_plural = 'GLA Members'

def save_user(sender, instance, **kwargs):
    print('\tin save_user()')
    print('kwargs = ',kwargs)
    print('user = ',instance.user)
    print('username = ',instance.username)
    instance.user = User.objects.filter(username=instance.username).first()
    instance.save()

# post_save.connect(save_user, sender=GLAMember)
