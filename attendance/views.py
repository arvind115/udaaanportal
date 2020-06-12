from django.shortcuts import render,redirect
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from .models import Attendance
from .forms import AttendanceForm
# Create your views here.
class AttendanceCreate(LoginRequiredMixin,CreateView):
  login_url = reverse_lazy('login')
  model = Attendance
  form_class = AttendanceForm
  template_name = 'attendancecreate.htm'
  success_url = reverse_lazy('home')
