from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Branch,CourseDetails
from .forms import CourseForm
# Create your views here.
def homeview(request,*args,**kwargs):
  return render(request,'exp.htm',{
    'form':CourseForm,
  })

def load_branches(request,*args,**kwargs):
  course_id = request.GET.get('course')
  print('in load_branches()...')
  print('GET = ', request.GET)
  branches = Branch.objects.filter(course=course_id)
  return render(request, 'load_branches.htm', {'branches':branches})

def createdview(request):
  print("inside created view")
  return render(request,'exp.htm',{})

class CourseCreateView(CreateView):
    model = CourseDetails
    form_class = CourseForm
    template_name = 'exp.htm'
    success_url = reverse_lazy('created')
