"""portal URL Configuration

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

from .views import home
from members.views import homeview,CourseCreateView,createdview, load_branches

urlpatterns = [
    # path('',homeview),
    path('form',CourseCreateView.as_view(),name='create_course'),
    path('form/created',createdview,name='created'),
    path('doesnotmatter', load_branches, name='ajax_load_branches'),


    path('admin/', admin.site.urls),
]
