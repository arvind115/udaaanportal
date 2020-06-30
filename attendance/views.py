from django.shortcuts import render,redirect, HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from datetime import datetime as dt

from members.models import Day

from .models import Attendance
from .forms import AttendanceForm

class AttendanceCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
  login_url = reverse_lazy('login')
  permission_required = ('attendance.add_attendance')
  model = Attendance
  form_class = AttendanceForm
  template_name = 'attendancecreate.htm'
  # success_url = reverse_lazy('home')

  def get(self,request,*args,**kwargs):
    # uncomment following lines in production
    # if Attendance.objects.filter(datetime__date=dt.today().date()).exists():
      # return HttpResponse("Today's attendance already uploaded.")
    # if not ( 4 <= dt.now().hour <= 6):
      # return HttpResponse('Attendance cannot be uploaded right now..')
    return super().get(request,*args,**kwargs)

  def get_form(self,*args,**kwargs):
    form = super().get_form(*args,**kwargs)
    members = Day.objects.filter(day=dt.today().strftime("%A")).first().glamember_set.all().order_by('year') 
    form.fields['members'].queryset = members
    return form

class AttendanceDetails(LoginRequiredMixin,DetailView):
  model = Attendance
  slug_field = 'slug'
  template_name = 'attendancedetails.htm'

