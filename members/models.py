from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Course(models.Model):
  class Meta:
    verbose_name = 'Course'
    verbose_name_plural = 'Courses'

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

  def __str__(self):
      return self.course

class Branch(models.Model):
  class Meta:
    verbose_name = 'Branch'
    verbose_name_plural = 'Branches'
  branch = models.CharField(
           max_length=50,
           blank=False,
           unique=False)
  course = models.ForeignKey(Course, on_delete=models.CASCADE)

  def __str__(self):
      return self.branch

class CourseDetails(models.Model):
  YEARS = (
    (1,1),(2,2),(3,3),(4,4)
  )
  class Meta:
    verbose_name = 'Course Detail'
    verbose_name_plural = 'Course Details'
  course = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)
  branch = models.ForeignKey(Branch, on_delete=models.CASCADE,null=True)
  year   = models.IntegerField(null=True,default=1,choices=YEARS)
  rollno = models.IntegerField(null=True)
  
class GLAMember(models.Model):
  class Meta:
    verbose_name = 'GLA Member'
    verbose_name_plural = 'GLA Member'
  gender_choices = (
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')
  )
  name      = models.CharField(max_length=50,blank=True,null=True)
  gender    = models.CharField(max_length=8,blank=True,null=True,choices=gender_choices)
  dob       = models.DateField(null=True,blank=True,auto_now=False, auto_now_add=False)
  email     = models.EmailField(max_length=50,null=True,blank=True)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', 
            message="Phone number must be entered in the format: '+999999999999'. Up to 12 digits allowed.")
  phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
  state = models.CharField(max_length=30,blank=True,null=True)
  city = models.CharField(max_length=50,blank=True,null=True)
  joined = models.DateField(blank=True,null=True,auto_now=False, auto_now_add=False)
  working_days = models.IntegerField(default=0,null=True,blank=True)
  photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None,null=True)
