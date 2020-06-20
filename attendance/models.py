from django.db import models
from django.db.models.signals import post_save, m2m_changed
from django.db import transaction


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
  # day = models.ForeignKey(Day, on_delete=models.CASCADE,null=True)
  members = models.ManyToManyField(GLAMember)
  datetime = models.DateTimeField(auto_now=False,null=True)

  objects = AttendanceManager()

  # def __str__(self):
  #   return self.datetime.strftime("%m/%d/%y, %H:%M:%S")


def update_working_days(sender, instance, action, reverse, *args, **kwargs):
    if action == 'post_add' and not reverse:
        for e in instance.members.all():
          e.working_days += 1
          e.save()
m2m_changed.connect(update_working_days, sender=Attendance.members.through)

