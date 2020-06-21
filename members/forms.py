from django import forms

from .models import Course,Branch,GLAMember,State,City

class GLAMemberForm(forms.ModelForm):
  state = forms.ModelChoiceField(queryset=State.objects.all(),help_text='select state',empty_label=' ')
  city = forms.ModelChoiceField(queryset=City.objects.none(),help_text='select city',empty_label=' ')
  course = forms.ModelChoiceField(queryset=Course.objects.all(),help_text='select course',empty_label=' ')
  branch = forms.ModelChoiceField(queryset=Branch.objects.none(),help_text='select branch',empty_label=' ')
  

  error_css_class = 'error'
  required_css_class = 'required'

  class Meta:
   model = GLAMember
   fields = ['username','name','gender','dob','email','phone','state','city','course','branch','year','rollno','joined_in',
              'working_days','preferred_days','photo']
   widgets = { 
        'name': forms.TextInput(attrs={'placeholder': ' '}),
        'email': forms.TextInput(attrs={'type':'email','placeholder':' '}),
        'dob':forms.DateInput(attrs={'type':'date'}),
        'phone': forms.TextInput(attrs={'placeholder':' '}),
        'rollno':forms.NumberInput(attrs={'placeholder':' '}),
        'joined_in':forms.DateInput(attrs={'type':'date'}),
    }
  # fields = '__all__'
  