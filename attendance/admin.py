from django.contrib import admin

# Register your models here.
from .models import Dummy,Attendance

class DummyAdmin(admin.ModelAdmin):
  list_display = ['datetime','day','weekday']
  class Meta:
    model = Dummy
  
  def day(self,obj):
    return obj.datetime.day
  def weekday(self,obj):
    return obj.datetime.weekday()

admin.site.register(Dummy,DummyAdmin)

admin.site.register(Attendance)
