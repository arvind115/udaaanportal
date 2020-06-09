from django.contrib import admin

# Register your models here.
from .models import Course,Branch,GLAMember,State,City,Day

class CourseAdmin(admin.ModelAdmin):
  list_display = ['course','duration']
  class Meta:
    model = Course

admin.site.register(Course,CourseAdmin)

class BranchAdmin(admin.ModelAdmin):
  list_display = ['branch','course']
  class Meta:
    model = Branch

admin.site.register(Branch,BranchAdmin)

class GLAMemberAdmin(admin.ModelAdmin):
  list_display = ['username','user','name','joined_in','pk',]
  class Meta:
    model = GLAMember

admin.site.register(GLAMember,GLAMemberAdmin)

class CityAdmin(admin.ModelAdmin):
  list_display = ['city','state']
  class Meta:
    model = City
admin.site.register(City,CityAdmin)

admin.site.register(State)

admin.site.register(Day)
