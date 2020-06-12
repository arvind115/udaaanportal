from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Branch,GLAMember,Course,State,City
from .forms import GLAMemberForm

# Create your views here.
def load_branches(request,*args,**kwargs):
  return render(request, 'load_branches.htm', {
    'branches':Branch.objects.filter(course=request.GET.get('course'))
  })
def load_cities(request,*args,**kwargs):
  print('kwargs = ',kwargs)
  return render(request, 'load_cities.htm', {
    'cities':City.objects.filter(state=request.GET.get('state')),
    'dashes':True
  })

class MemberCreateView(LoginRequiredMixin,CreateView):
  login_url = reverse_lazy('login')
  model = GLAMember
  form_class = GLAMemberForm
  template_name = 'membercreate.htm'

  def get(self,request,*args,**kwargs):
    if GLAMember.objects.filter(user=request.user).exists():
    # if request.user.glamember:
      return render(request,'snippets/profileexists.htm',{})
    return super(MemberCreateView,self).get(request,*args,**kwargs)

  def post(self,request,*args, **kwargs):
    form = GLAMemberForm(request.POST,request.FILES)
    print('....in post()')
    print('POST = ',request.POST)
    print('FILES = ', request.FILES)
    course_id = request.POST.get('course', None)
    if course_id is not None:
      form.fields['branch'].queryset = Branch.objects.filter(course_id=course_id).order_by('branch')
    state_id = request.POST.get('state',None)
    if state_id is not None:
      form.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('city')
    if form.is_valid():
        print('\tFORM VALID.')
        # Call parent form_valid to create model record object
        # super(MemberCreateView,self).form_valid(form)
        self.form_valid(form)
        # obj = form.save(commit=False)
        # obj.user = request.user
        # obj.save()
        # user = request.user
        # user.glamember = form.save()
        # user.save()
        # form.fields['user'] = User.objects.filter(pk=self.request.user.id).first()
        # form.save()
        messages.success(request, 'Member profile created successfully!')      
        return HttpResponseRedirect(self.get_success_url())
    # Form is invalid , set object to None, since class-based view expects model record object
    print('\t FORM INVALID')
    self.object = None
    return super(MemberCreateView,self).form_invalid(form)

  # def get_context_data(self, **kwargs):
  #   form = kwargs.get('form') or super(MemberCreateView,self).get_form()
  #   if self.request.method == 'GET':
  #     print('in CreateView gcd() with GET')
  #     print('form length = ',len(str(form)))
  #     # print('req_user',self.request.user)
  #     # print('db_user',User.objects.filter(pk=self.request.user.id).first())
  #     # form.fields['city'].queryset =  City.objects.none()
  #     # form.fields['branch'].queryset = Branch.objects.none()
  #     print('form length = ',len(str(form)))
  #   '''else:
  #     print('in gcd() with POST')
  #     form.fields['city'].queryset = City.objects.filter(state_id=form.cleaned_data.get('state')) 
  #     form.fields['branch'].queryset = Branch.objects.filter(course_id=form.cleaned_data.get('course'))'''
  #   kwargs['form'] = form 
  #   return super().get_context_data(**kwargs)

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
  def form_valid(self, form):
    form.instance.user = self.request.user
    super().form_valid(form)
    # messages.success(self.request, 'Member profile created successfully!')        
    return HttpResponseRedirect(self.get_success_url())

  def get_success_url(self):
    return reverse('memberdetails',kwargs={'slug':self.request.POST.get('username')})
        
  # def form_invalid(self,form):
  #   print('in form invalid()...')
  #   # Add action to invalid form phase
  #   super(MemberCreateView,self).form_invalid(form)
  #   return self.render_to_response(self.get_context_data(form=form))
  


# seed into db  

class MemberUpdateView(LoginRequiredMixin,UpdateView):
  login_url = reverse_lazy('login')
  model = GLAMember
  fields = ['username','name','gender','dob','email','phone','state','city','course','branch','year','rollno','joined_in',
              'working_days','preferred_days','photo']
  # form_class = GLAMemberForm
  slug_field = 'username'
  template_name = 'membercreate.htm'

  def get(self,request,*args,**kwargs):
    print('in GET of UpdateView')
    if not GLAMember.objects.filter(user=request.user).exists():
      return redirect('membercreate')
    if not str(kwargs.get('slug')) == str(request.user):
      return HttpResponse('You are NOT authorised to edit other members details')
    #   profile exists for requset.user, logged in user is request.user
    return super(MemberUpdateView,self).get(request,*args,**kwargs)

  # def get_object(self,*args,**kwargs):
  #   obj = super().get_object(*args,**kwargs)
  #   print('in get_object()')
  #   print(kwargs)
  #   print(self.request.GET)
  # #   # print(type(obj.state))
  # #   # cities = obj.state.city_set.all()
  # #   # print(cities)
  # #   # print(type(obj.city))
  #   return obj

  def get_form(self,*args,**kwargs):
    form =  super().get_form(*args,**kwargs)
    print('in get_form')
    print(len(str(form)))
    # state = form.fields['state']
    # print(state)
    form.fields['city'].queryset = City.objects.none()
    form.fields['branch'].queryset = Branch.objects.none()
    print(len(str(form)))
    return form

  # def post(self,*args, **kwargs):
  #   form = GLAMemberForm(self.request.POST,self.request.FILES)
  #   print('....in UpdateView post()')
  #   print('POST = ',self.request.POST)
  #   print('FILES = ', self.request.FILES)
  #   course_id = self.request.POST.get('course', None)
  #   if course_id is not None:
  #     form.fields['branch'].queryset = Branch.objects.filter(course_id=course_id).order_by('branch')
  #   state_id = self.request.POST.get('state',None)
  #   if state_id is not None:
  #     form.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('city')
  #   if form.is_valid():
  #       print('\tFORM VALID.')
  #       # Call parent form_valid to create model record object
  #       super(MemberUpdateView,self).form_valid(form)
  #       # self.form_valid(form)
  #       messages.success(self.request, 'Member profile created successfully!')      
  #       return HttpResponseRedirect(self.get_success_url())
  #   # Form is invalid , set object to None, since class-based view expects model record object
  #   print('\t FORM INVALID')
  #   self.object = None
  #   return super(MemberUpdateView,self).form_invalid(form)

  # def get_context_data(self, **kwargs):
  #   kwargs = super().get_context_data(**kwargs)
  #   form = kwargs.get('form') or super(MemberUpdateView,self).get_form()
  #   if self.request.method == 'GET':
  #     print('UpdateView gcd() with GET')
  #     print('kwargs', kwargs)
  #     print('form',len(str(form)))
  #   else:
  #     print('in gcd() with POST')
  #     print('POST = ',self.request.POST)
  #     print('FILES = ', self.request.FILES)
  #     form = GLAMemberForm(self.request.POST,self.request.FILES)
  #     form.fields['city'].queryset = City.objects.filter(state_id=self.request.POST.get('state')) 
  #     form.fields['branch'].queryset = Branch.objects.filter(course_id=self.request.POST.get('course'))
  #     print('form',len(str(form)))
  #     if form.is_valid():
  #       print('\tVALID FORM')
  #       # self.form_valid(form)
  #   kwargs['form'] = form 
  #   return kwargs
  
  # def form_valid(self, form):
  #   form.instance.user = self.request.user
  #   super(MemberUpdateView,self).form_valid(form)
  #   messages.success(self.request, 'Member profile updated successfully!')        
  #   return HttpResponseRedirect(self.get_success_url())


class MemberDetails(DetailView):
  model = GLAMember
  slug_field = 'username'
  template_name = 'memberdetails.htm'

  



