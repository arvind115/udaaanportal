from django.db import models

from members.models import GLAMember,Day

class Attendance(models.Model):
  # day = models.ForeignKey(Day, on_delete=models.CASCADE,null=True)
  members = models.ManyToManyField(GLAMember)
  datetime = models.DateTimeField(auto_now=False, auto_now_add=False,null=True)
  
class Dummy(models.Model):
  datetime = models.DateTimeField(auto_now=False, auto_now_add=False)

  # def __str__(self):
  #   return self.datetime
  
