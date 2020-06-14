from django.shortcuts import render,redirect
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from datetime import datetime as dt
from members.models import Day

from .models import Attendance
from .forms import AttendanceForm

DAYS = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

# Create your views here.
class AttendanceCreate(LoginRequiredMixin,CreateView):
  login_url = reverse_lazy('login')
  model = Attendance
  form_class = AttendanceForm
  template_name = 'attendancecreate.htm'
  success_url = reverse_lazy('home')

  # def get(self,request,*args,**kwargs):
    # print('in GET of AttendanceCreateView')
    # print('today is ->',Day.objects.filter(pk=dt.now().weekday()+1).first())
    # return super().get(request,*args,**kwargs)

  def get_form(self,*args,**kwargs):
    form = super().get_form(*args,**kwargs)
    # print("in get_form() of AttendanceCreate view")
    qs = Day.objects.filter(day=DAYS[dt.now().weekday()]).first().glamember_set.all().order_by('year') 
    # print('qs = ',qs)
    form.fields['members'].queryset = qs
    return form
