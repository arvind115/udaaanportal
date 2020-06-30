from django import forms 

from .models import Attendance
from members.models import GLAMember

class AttendanceForm(forms.ModelForm):
  members = forms.ModelMultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple(),
        queryset = GLAMember.objects.none())

  class Meta:
    model = Attendance
    fields = ('members',)
