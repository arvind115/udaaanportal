1) In MemberUpdateView, whole queryset of City & Branch is fetched from db. Need to explictitly set to .none() in get_form()
### Try overriding __init__() method of GLAMemberForm, instead of post() in MemberCreate 


2) In AttendanceForm class, Members.objects.all() is passed off to queryset, all the fields are passed, create a ModelManager method to only return the 'id','name', 'course','branch','year'.

3) Year options should be populated after a Course has been selected. fixit.

4) fix year range issue in get_by_year() in AttendanceManager in 'attendance'

# Add AJAX

# Add custom templates for 404,500 etc.

