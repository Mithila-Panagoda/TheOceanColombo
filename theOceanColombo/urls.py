"""theOceanColombo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.directHome),
    url(r'^loadaddsupplier/', views.directaddsupplier),
    url(r'^addsupplier/', views.addsupplier),
    url(r'^addstock/', views.directaddstock),
    url(r'^inventory/', views.directinventory),
    url(r'^directmessages/', views.directmessages),
    url(r'^addmessages/', views.addmessages),
    url(r'^sendmessages/', views.sendmessages),
    url(r'^purchaseOrders/', views.directpurchaseOrders),
    url(r'^suppliers/', views.directsuppliers),
    url(r'^createcustomergroups/', views.directcreatecustomergroups),
    url(r'customerlogin/', views.custloign),
    url(r'^logout', views.logout, name="log"),
    url(r'^addDeductions/', views.addAdditionalDeductions),
    url(r'^addEarnings/', views.addEarnings),
    url(r'^additionsDeductions/', views.additionsDeductions),
    url(r'^EPFOfWhoseSalaryIsNeeded', views.EPFOfWhoseSalaryIsNeeded),
    url(r'^EPFToCalculateSalary', views.EPFToCalculateSalary),
    url(r'^PayrollManagementHome', views.directPayrollManagementHome),
    url(r'^PaySlip', views.dirPaySlip),
    url(r'^SalaryDetailsOfAllEmployees', views.dirSalaryDetailsOfAllEmployees),
    url(r'^SalaryHistoryOfEmployee', views.dirSalaryHistoryOfEmployee),
    url(r'^UpdateAdditionsOrDeductions', views.dirUpdateAdditionsOrDeductions),
    url(r'^continuousReport', views.dirContinuousReport),
    url(r'^HousekeepingReport', views.dirHousekeepingReport),
    url(r'^InsertRoomDetails', views.dirInsertRoomDetails),
    url(r'^roomDetails', views.dirRoomDetails),
    url(r'^roomManagementHome', views.dirRoomManagementHome),
    url(r'^updateRoomDetails', views.dirUpdateRoomDetails)

]

