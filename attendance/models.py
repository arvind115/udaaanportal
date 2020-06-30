from django.db import models
from django.db.models.signals import post_save, m2m_changed
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from datetime import datetime as dt

from members.models import GLAMember,Day

class AttendanceManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter()

    def get_by_week_day(self,dayno=2,user=None):
      ''' Sunday: 1... Saturday: =7'''
      if user is not None:
        return user.glamember.attendance_set.all().filter(datetime__week_day=dayno)
      return super().get_queryset().filter(datetime__week_day=dayno)

    def get_by_month(self,monthno=1,user=None):
      '''January: 1 ... December:12 '''
      if user is not None:
        return user.glamember.attendance_set.all().filter(datetime__month=monthno)
      return super().get_queryset().filter(datetime__month=monthno)

    def get_by_year(self,yearno=2020,user=None):
      '''minYear: 2020, maxYear: current year...'''
      if user is not None:
        return user.glamember.attendance_set.all().filter(datetime__year=yearno)
      return super().get_queryset().filter(datetime__year=yearno)

    def get_by_course(self,course):
      '''course should be an instance of members.models.Course '''
      return self.get_queryset().filter(members__course=course)

    def get_by_branch(self,branch):
      '''branch should be an instance of members.models.Branch'''
      return self.get_queryset().filter(members__branch=branch)
    
    def get_by_course_year(self,year=3):
      '''year should be in range of 1-4'''
      return self.get_queryset().filter(members__year=year)

    def get_by_gender(self,gender='Male'):
      return self.get_queryset().filter(members__gender=gender)

class Attendance(models.Model):
  slug = models.SlugField(max_length=11,null=True,blank=True,default='some date')
  members = models.ManyToManyField(GLAMember)
  datetime = models.DateTimeField(auto_now=False,null=True)
  present = models.IntegerField(null=True,blank=True,default=0)
  total = models.IntegerField(null=True,blank=True,default=0)

  objects = AttendanceManager()

  def __str__(self):
    DATE_FORMAT = "%Y/%m/%d"
    TIME_FORMAT = '%H:%M:%S'
    return self.datetime.strftime("%s %s" % (DATE_FORMAT, TIME_FORMAT))

  def get_absolute_url(self):
      return reverse('attendancedetails', kwargs={'slug': self.slug })

def update_working_days(sender, instance, action, reverse, *args, **kwargs):
    if action == 'post_add' and not reverse:
      instance.present = instance.members.all().count()
      instance.total = Day.objects.filter(day=dt.today().strftime("%A")).first().glamember_set.count()
      instance.save()
      for member in instance.members.all():
        member.working_days += 1
        member.save()
m2m_changed.connect(update_working_days, sender=Attendance.members.through)

def sets_datetime(sender,instance,created,*args,**kwargs):
  if created:
    instance.datetime = timezone.now()
    instance.slug = instance.datetime.strftime('%s'%("%Y-%b-%d"))
    instance.save()
  
post_save.connect(sets_datetime,sender=Attendance)

