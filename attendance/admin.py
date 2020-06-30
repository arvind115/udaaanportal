from django.contrib import admin

# Register your models here.
from .models import Attendance

class AttendanceAdmin(admin.ModelAdmin):
  list_display = ['datetime','slug']
  # readonly_fields = ('datetime',)

  def members(self,obj):
    return str(obj.members.all().first().username)

admin.site.register(Attendance, AttendanceAdmin)
