from django.shortcuts import render,redirect, HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView

from datetime import datetime as dt
from members.models import Day

from .models import Attendance
from .forms import AttendanceForm

DAYS = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

# Create your views here.
class AttendanceCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
  login_url = reverse_lazy('login')
  permission_required = ('attendance.add_attendance')
  model = Attendance
  form_class = AttendanceForm
  template_name = 'attendancecreate.htm'
  success_url = reverse_lazy('home')

  def get(self,request,*args,**kwargs):
    # uncomment following lines in production
    # if not ( 4 <= dt.now().hour <= 6):
      # return HttpResponse('Attendance cannot be uploaded right now..')
    return super().get(request,*args,**kwargs)

  def get_form(self,*args,**kwargs):
    # print(Attendance.objects.get_by_year(yearno=2020))#,user=self.request.user))
    form = super().get_form(*args,**kwargs)
    # print("in get_form() of AttendanceCreate view")
    qs = Day.objects.filter(day=DAYS[dt.now().weekday()]).first().glamember_set.all().order_by('year') 
    # print('qs = ',qs)
    form.fields['members'].queryset = qs
    return form
