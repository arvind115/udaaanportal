from django import forms 

from .models import Attendance
from members.models import GLAMember

class DateInputWidget(forms.DateInput):
  input_type = 'date'

class AttendanceForm(forms.ModelForm):
  # datetime = forms.DateField(widget=DateInputWidget())
  members = forms.ModelMultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple(),
        queryset = GLAMember.objects.none())

  class Meta:
    model = Attendance
    # fields = ('members') #datetime field should be handled in GET & POST
    fields = ('members',)
    widgets = { 'DateInputWidget': DateInputWidget }
