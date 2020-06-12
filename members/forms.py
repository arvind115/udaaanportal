from django import forms

from .models import Branch,GLAMember,City,Day

class DateInputWidget(forms.DateInput):
  input_type = 'date'

class GLAMemberForm(forms.ModelForm):
  # DAYS=(
  #   ('Monday','Monday'),
  #   ('Tuesday','Tuesday'),
  #   ('Wednesday','Wednesday'),
  #   ('Thursday','Thursday'),
  #   ('Friday','Friday'),
  #   ('Saturday','Saturday'),
  #   ('Sunday','Sunday'),
  # )
  # preferred_days =  forms.ModelMultipleChoiceField(
  #       required=True,
  #       widget=forms.CheckboxSelectMultiple(),
  #       queryset = Day.objects.all()
  # )
  # preferred_day = forms.MultipleChoiceField(
  #   choices=[(option, option) for option in
  #            Day.objects.all()], widget=forms.CheckboxSelectMultiple(),
  #   label="Days", required=True, error_messages={'required': 'myRequiredMessage'})
  city = forms.ModelChoiceField(queryset=City.objects.none())
  branch = forms.ModelChoiceField(queryset=Branch.objects.none())
  dob = forms.DateField(widget=DateInputWidget())
  joined_in = forms.DateField(widget=DateInputWidget())

  class Meta:
   model = GLAMember
   fields = ['username','name','gender','dob','email','phone','state','city','course','branch','year','rollno','joined_in',
              'working_days','preferred_days','photo']
   widgets = { 'DateInputWidget': DateInputWidget }
  # fields = '__all__'
  
  # def __init__(self, *args, **kwargs):
  #   super().__init__(*args, **kwargs)
  #   print('\t in form constructor()')
  #   print('form data = ',self.data)
  #   if 'course' in self.data:
  #     try:
  #         course_id = int(self.data.get('course'))
  #         self.fields['branch'].queryset = Branch.objects.filter(course_id=course_id).order_by('branch')
  #     except (ValueError, TypeError):
  #         pass  # invalid input from the client; ignore and fallback to empty branch queryset
  #   elif self.instance.pk:
  #       self.fields['branch'].queryset = self.instance.course.branch_set.order_by('branch')
  #   # self.fields['username'].disabled = True
  #   self.fields['city'].queryset = City.objects.none()
  #   self.fields['branch'].queryset = Branch.objects.none()

  # def clean(self,*args,**kwargs):
  #   print('in is_valid()')
  #   return super(GLAMemberForm,self).clean(*args,**kwargs)
