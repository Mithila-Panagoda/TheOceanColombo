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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.directHome),
    url(r'^complaint1/', views.complaintFront),
    url(r'^ComplaintFrontdata/', views.complaintFrontdata),
    url(r'^complaint2/', views.complaintReply),
    url(r'^complaint3/', views.complaintTyping),
    url(r'^complaint4/', views.complaintCheckReply),
    url(r'^complaint5/', views.complaintUpdateReply),
    url(r'^complaint6/', views.complaintView),
    url(r'^Expenses1/', views.addExpenses),
    url(r'^addExpensesACC/', views.addExpensesACC),
    url(r'^Expenses2/', views.Expenseslist),
    url(r'^AddRevenue/', views.AddRevenue),
    url(r'^addrevenueacc/', views.AddRevenueAcc),
    url(r'^revenueList/', views.RevenueList),
    url(r'^Capital/', views.Capital),
    url(r'^CapitalACC/', views.CapitalAcc),
    url(r'^ViewCapital/', views.ViewCapital),


    url(r'^Expenses6/', views.update6),
    url(r'^Expenses7/', views.ledgers),
    url(r'^Expenses8/', views.ledgersView),
    url(r'^Expenses9/', views.reports9),
    url(r'^Expenses10/', views.reportsdisplay),
    url(r'^addsupplier/', views.directaddsupplier),
    url(r'^addstock/', views.directaddstock),
    url(r'^inventory/', views.directinventory),
    url(r'^purchaseOrders/', views.directpurchaseOrders),
    url(r'^suppliers/', views.directsuppliers),
    url(r'^createcustomergroups/', views.directcreatecustomergroups),
    url(r'customerlogin/', views.custloign),
 
    url(r'^logout', views.logout, name="log"),
    url(r'^logout/', views.logout),

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
    url(r'^loadaddmeal/', views.loadaddmeal),
    url(r'^loadupdatemeal/',views.loadupdatemeal),
    url(r'^updatemeal/',views.updatemeal),
    url(r'^addmeal/',views.addmeal),
    url(r'^addbeverage/',views.addbeverage),
    url(r'^updatemeal/',views.updatemeal),
    url(r'^updatebeverage/',views.updatebeverage),
    url(r'^updateRoomDetails', views.dirUpdateRoomDetails),
    url(r'^mealmngt/', views.mealmngt),
    url(r'^custbillhistory/',views.custbillhistory),
    url(r'^getmeals/',views.getmeals),
    url('InsertRooms',views.InsertRooms, name="InsertRooms"),
    url(r'^addmeal/', views.addmeal),
    url(r'^addbeverage/',views.addbeverage),
    url(r'^updatemeal/',views.updatemeal),
    url(r'^updatebeverage/',views.updatebeverage),
    url(r'^updateRoomDetails', views.dirUpdateRoomDetails),
    url(r'^loadcustpos', views.loadcustpos),
    url(r'^bookvehicle/',views.bookvhecicale),
    url(r'^updatebeverage/',views.updatebeverage),
    url(r'^updateRoomDetails', views.dirUpdateRoomDetails),
    url(r'^customerRegistration/', views.custreg),
    url(r'attendance/', views.attendance),
    url(r'search/', views.search),
    url(r'searchresults/', views.searchresults),
    url(r'^newEmployee/', views.Newemployee),
    url(r'^viewEmployee/', views.Viewemployee),
    url(r'^promoManagement/', views.Promomanagement),
    url(r'^updatePromo/', views.Updatepromo),
    url(r'^HireNew/', views.loadNewemployee)
    url(r'^loadcustpos', views.loadcustpos)
    url(r'^bookvehicle/',views.bookvhecicale),
    url(r'^updatebeverage/',views.updatebeverage),
    url(r'^updateRoomDetails', views.dirUpdateRoomDetails),
    url(r'^selectRoom/', views.selectroom),
    url(r'^confirmBooking/', views.confirmbooking),
    url(r'^cancelBooking/', views.cancelbooking),
    url(r'^updateBooking/', views.updatebooking)

]

urlpatterns += staticfiles_urlpatterns()

