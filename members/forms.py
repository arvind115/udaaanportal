from django import forms

from .models import CourseDetails,Branch

class CourseForm(forms.ModelForm):
  class Meta:
    model = CourseDetails
    fields = ('course','branch','year')

  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'course' in self.data:
              try:
                  course_id = int(self.data.get('course'))
                  self.fields['branch'].queryset = Branch.objects.filter(course_id=course_id).order_by('branch')
              except (ValueError, TypeError):
                  pass  # invalid input from the client; ignore and fallback to empty branch queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.course.branch_set.order_by('branch')

