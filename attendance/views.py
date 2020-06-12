from django.shortcuts import render
from djago.views.generic.edit import CreateView

from .models import Attendance
# Create your views here.
class AttendanceCreate(CreateView):
  model = Attendance
  template_name = 'attendancecreate.htm'
