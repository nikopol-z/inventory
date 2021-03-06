"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
import inv.views
import inv.models
import inv.forms

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', inv.views.main),
    path('doc_type_error/', inv.views.doc_type_error),
    path('catlg_type_error/', inv.views.catlg_type_error),
    path('reg_type_error/', inv.views.reg_type_error),
    re_path('doc/(?P<doc_name>\w+)/$', inv.views.doc_list),
    re_path('doc/(?P<doc_name>\w+)/(?P<doc_id>\w+)/$', inv.views.doc_form),
    re_path('(?P<obj_type_name>\w+)/(?P<obj_name>\w+)/(?P<obj_id>\w+)/status/(?P<operation>\w+)/(?P<status>\d)/$', inv.views.operation_status),
    re_path('catlg/(?P<catlg_name>\w+)/$', inv.views.catlg_list),
    re_path('catlg/(?P<catlg_name>\w+)/(?P<catlg_id>\w+)/$', inv.views.catlg_form),
    re_path('doc/(?P<doc_name>\w+)/(?P<doc_id>\w+)/reg/$', inv.views.doc_reg_recs),
    re_path('report/current_location/$', inv.views.report_current_location, {'dev_id': 4, 'date_to': '2018-10-30 03:00:00'}),
]
