from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User

from django.forms import DateInput

from .models import Branch,GLAMember,Course,State,City
from .forms import GLAMemberForm

# Create your views here.
def load_branches(request,*args,**kwargs):
  return render(request, 'load_branches.htm', {
    'branches':Branch.objects.filter(course=request.GET.get('course'))})

def load_cities(request,*args,**kwargs):
  return render(request, 'load_cities.htm', {
    'cities':City.objects.filter(state=request.GET.get('state'))})

class MemberCreateView(LoginRequiredMixin,CreateView):
  login_url = reverse_lazy('login')
  model = GLAMember
  form_class = GLAMemberForm
  template_name = 'membercreate.htm'

  def get(self,request,*args,**kwargs):
    if GLAMember.objects.filter(user=request.user).exists():
      return render(request,'snippets/profileexists.htm',{})
    return super(MemberCreateView,self).get(request,*args,**kwargs)

  def post(self,request,*args, **kwargs):
    form = GLAMemberForm(request.POST,request.FILES)
    course_id = request.POST.get('course', None)
    if course_id is not None:
      form.fields['branch'].queryset = Branch.objects.filter(course_id=course_id).order_by('branch')
    state_id = request.POST.get('state',None)
    if state_id is not None:
      form.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('city')
    if form.is_valid():
        self.form_valid(form)
        messages.success(request, 'Member profile created successfully!')      
        return HttpResponseRedirect(self.get_success_url())
    # Form is invalid , set object to None, since class-based view expects model record object
    self.object = None
    return super(MemberCreateView,self).form_invalid(form)
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    super().form_valid(form)     
    return HttpResponseRedirect(self.get_success_url())

  def get_success_url(self):
    return reverse('memberdetails',kwargs={'slug':self.request.POST.get('username')})
        
class MemberUpdateView(LoginRequiredMixin,UpdateView):
  login_url = reverse_lazy('login')
  model = GLAMember
  fields = ['username','name','gender','dob','email','phone','state','city','course','branch','year','rollno','joined_in',
              'working_days','preferred_days','photo']
  # form_class = GLAMemberForm
  slug_field = 'username'
  template_name = 'membercreate.htm'

  def get(self,request,*args,**kwargs):
    if not GLAMember.objects.filter(user=request.user).exists():
      return redirect('membercreate')
    if not str(kwargs.get('slug')) == str(request.user):
      return HttpResponse('You are NOT authorised to edit other members details')
    return super(MemberUpdateView,self).get(request,*args,**kwargs)

 
  def get_form(self,*args,**kwargs):
    form =  super().get_form(*args,**kwargs)
    print(len(str(form)))
    form.fields['city'].queryset = City.objects.none()
    form.fields['branch'].queryset = Branch.objects.none()
    form.fields['dob'].widget = DateInput(attrs={'type':'date'})
    form.fields['joined_in'].widget = DateInput(attrs={'type':'date'})
    return form

class MemberDetails(DetailView):
  model = GLAMember
  slug_field = 'username'
  template_name = 'memberdetails.htm'

  



