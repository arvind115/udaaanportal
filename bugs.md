1) In MemberUpdateView, whole queryset of City & Branch is fetched from db. Need to explictitly set to .none() in get_form()

2) In AttendanceForm class, Members.objects.all() is passed off to queryset, all the fields are passed, create a ModelManager method to only return the 'id','name', 'course','branch','year'.

3) Configure permissions, to allow only a permitted user to upload attendance.

