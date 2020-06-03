from django.contrib import admin

# Register your models here.
from .models import Course,Branch,CourseDetails

class CourseAdmin(admin.ModelAdmin):
  list_display = ['course','duration']
  class Meta:
    model = Course

class BranchAdmin(admin.ModelAdmin):
  list_display = ['branch','course']
  class Meta:
    model = Branch

admin.site.register(Course,CourseAdmin)
admin.site.register(Branch,BranchAdmin)
admin.site.register(CourseDetails)
