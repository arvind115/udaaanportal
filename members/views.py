from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Branch,GLAMember,Course,State,City
from .forms import GLAMemberForm

# Create your views here.
def load_branches(request,*args,**kwargs):
  return render(request, 'load_branches.htm', {
    'branches':Branch.objects.filter(course=request.GET.get('course'))
  })
def load_cities(request,*args,**kwargs):
  return render(request, 'load_cities.htm', {
    'cities':City.objects.filter(state=request.GET.get('state'))
  })

class MemberCreateView(LoginRequiredMixin,CreateView):
  login_url = reverse_lazy('login')
  model = GLAMember
  form_class = GLAMemberForm
  template_name = 'membercreate.htm'
  success_url = reverse_lazy('home')

  # def get(self,request,*args,**kwargs):
  #   return render(request,self.template_name,{
  #     'form':GLAMemberForm(initial={
  #       'branch':Branch.objects.none()
  #     }),
  #   })

  # def post(self,request,*args, **kwargs):
  #   form = GLAMemberForm(request.POST,request.FILES)
  #   print('....in post()')
  #   print('POST = ',request.POST)
  #   print('FILES = ', request.FILES)
  #   # course_id = request.POST.get('course', None)
  #   # if course_id is not None:
  #   #   form.fields['branch'].queryset = Branch.objects.filter(course_id=course_id).order_by('branch')
  #   # state_id = request.POST.get('state',None)
  #   # if state_id is not None:
  #   #   form.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('city')
  #   if form.is_valid():
  #       print('here.')
  #       # Call parent form_valid to create model record object
  #       super(MemberCreateView,self).form_valid(form)
  #       messages.success(request, 'Member profile created successfully!')      
  #       return HttpResponseRedirect(self.get_success_url())
  #   # Form is invalid , set object to None, since class-based view expects model record object
  #   print('form INVALID')
  #   self.object = None
  #   return super(MemberCreateView,self).form_invalid(form)

  def get_context_data(self, **kwargs):
    form = kwargs.get('form') or super(MemberCreateView,self).get_form()
    if self.request.method == 'GET':
      form.fields['city'].queryset =  City.objects.none()
      form.fields['branch'].queryset = Branch.objects.none()
    else:
      form.fields['city'].queryset = City.objects.filter(state_id=form.cleaned_data.get('state')) 
      form.fields['branch'].queryset = Branch.objects.filter(course_id=form.cleaned_data.get('course'))
    kwargs['form'] = form 
    return super().get_context_data(**kwargs)

  # def get_initial(self):
  #   initial = super(MemberCreateView,self).get_initial()
  #   initial['city'].queryset = City.objects.none()
  #   return initial

  # def get_form(self):
  #   # print('in get_form()..')
  #   form = super(MemberCreateView, self).get_form()
  #   initial_base = self.get_initial() 
  #   initial_base['username'] = self.request.user
  #   form.initial = initial_base
  #   # form.fields['username'].disabled = True
  #   form.fields['state'].queryset = State.objects.all()
  #   form.fields['city'].queryset = City.objects.none()
  #   form.fields['course'].queryset = Course.objects.all()
  #   form.fields['branch'].queryset = Branch.objects.none()
  #   return form

  # def form_valid(self,form):
  #   print('\tin form_valid()')
  #   super(MemberCreateView,self).form_valid(form)
  #   # Add action to valid form phase
  #   messages.success(self.request, 'Member profile created successfully!')        
  #   return HttpResponseRedirect(self.get_success_url())  

  def get_success_url(self):
    return reverse('memberdetails',kwargs={'slug':self.request.POST.get('username')})
        
  # def form_invalid(self,form):
  #   print('in form invalid()...')
  #   # Add action to invalid form phase
  #   super(MemberCreateView,self).form_invalid(form)
  #   return self.render_to_response(self.get_context_data(form=form))
  


# seed into db
#course first
# for course in (('btech','B.Tech'),
#     ('mtech','M.Tech'),
#     ('bphrama','B.Pharma'),
#     ('mpharma','M.Pharma'),
#     ('biotech','Biotech'),
#     ('bba','BBA'),
#     ('mba','MBA'),
#     ('bca','BCA'),
#     ('mca','MCA'),
#     ('polytechnic','Polytechnic')):
  

#then branches

class MemberDetails(DetailView):
  model = GLAMember
  slug_field = 'username'
  template_name = 'memberdetails.htm'

  



