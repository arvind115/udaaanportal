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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.views import LoginView

from .views import home,registerview, logoutview
from members.views import MemberCreateView,MemberUpdateView, load_branches, load_cities, MemberDetails

urlpatterns = [
    path('',home,name='home'),
    path('login', LoginView.as_view(), {'template_name': 'login.htm'}, name='login'),
    path('register',registerview,name='register'),
    path('logout',logoutview,name='logout'),

    path('membercreate',MemberCreateView.as_view(),name='membercreate'),
    path('memberupdate/<slug:slug>',MemberUpdateView.as_view(),name='memberupdate'),
    path('memberdetails/<slug:slug>',MemberDetails.as_view(),name='memberdetails'),

    path('doesnotmatter', load_branches, name='ajax_load_branches'),
    path('doesnotmatter2', load_cities, name='ajax_load_cities'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
