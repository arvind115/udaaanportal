from django.db import models
from django.db.models.signals import post_save, m2m_changed
from django.db import transaction


from members.models import GLAMember,Day

class Attendance(models.Model):
  # day = models.ForeignKey(Day, on_delete=models.CASCADE,null=True)
  members = models.ManyToManyField(GLAMember)
  datetime = models.DateTimeField(auto_now=False, auto_now_add=False,null=True)

def update_working_days(sender, instance, action, reverse, *args, **kwargs):
    if action == 'post_add' and not reverse:
        for e in instance.members.all():
          e.working_days += 1
          e.save()
m2m_changed.connect(update_working_days, sender=Attendance.members.through)


