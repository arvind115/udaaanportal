"""project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path, reverse_lazy
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views

from .views import home,registerview, activate, logoutview
from attendance.views import AttendanceCreate, AttendanceDetails
from members.views import MemberCreateView,MemberUpdateView, load_branches, load_cities, MemberDetails

urlpatterns = [
    path('',home,name='home'),
    path('login', auth_views.LoginView.as_view(), {'template_name': 'login.htm'}, name='login'),
    path('register',registerview,name='register'),
    path('activate/<uidb64>/<token>/',activate,name='activate'),
    path('logout',logoutview,name='logout'),

    path('membercreate',MemberCreateView.as_view(),name='membercreate'),
    path('memberupdate/<slug:slug>',MemberUpdateView.as_view(),name='memberupdate'),
    path('memberdetails/<slug:slug>',MemberDetails.as_view(),name='memberdetails'),

    path('doesnotmatter', load_branches, name='ajax_load_branches'),
    path('doesnotmatter2', load_cities, name='ajax_load_cities'),

    re_path(r'^attendancecreate$',AttendanceCreate.as_view(),name='attendancecreate'),
    # path('attendancedetails/<int:year>/<int:month>/<int:day>',AttendanceDetails.as_view(),name='attendancedetails'),
    # re_path(r'^attendancedetails/(?P<slug>[0-9]{4}/[0-9]{2}/[0-9]{2})/$',AttendanceDetails.as_view(),name='attendancedetails'),
    path('attendancedetails/<slug:slug>',AttendanceDetails.as_view(),name='attendancedetails'),

    path('admin/', admin.site.urls),
    path('passwordreset',auth_views.PasswordResetView.as_view(
        template_name = 'accounts/passwordreset.htm'
    ),name='passwordreset'),
    path('passwordresetsent',auth_views.PasswordResetDoneView.as_view(
        template_name = 'accounts/passwordresetsent.htm'
    ),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(
        template_name = 'accounts/passwordresetconfirm.htm'
    ),name='password_reset_confirm'),
    path('passwordresetcomplete',auth_views.PasswordResetCompleteView.as_view(
        template_name = 'accounts/passwordresetcomplete.htm'
    ),name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
