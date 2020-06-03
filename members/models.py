from django.db import models

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
  class Meta:
    verbose_name = 'Course Detail'
    verbose_name_plural = 'Course Details'
  course = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)
  branch = models.ForeignKey(Branch, on_delete=models.CASCADE,null=True)
  year   = models.IntegerField(null=True,default=1)
  rollno = models.IntegerField(null=True)
  
class GLAMember(models.Model):
  pass
