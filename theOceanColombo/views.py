from django.http import HttpResponseRedirect
from django.shortcuts import render
import pyrebase
from django.contrib import auth
#from firebase import firebase

firebaseconfig = {
    'apiKey': "AIzaSyBew42hA7iZHy7zs47WMqIg-GSBnxP-ttM",
    'authDomain': "theoceancolombo-c128a.firebaseapp.com",
    'databaseURL': "https://theoceancolombo-c128a.firebaseio.com",
    'projectId': "theoceancolombo-c128a",
    'storageBucket': "theoceancolombo-c128a.appspot.com",
    'messagingSenderId': "925636680144",
    'appId': "1:925636680144:web:da1ab5d4f3b0d3231b01d5",
    'measurementId': "G-YH7TV23J8J"
}
firebase = pyrebase.initialize_app(firebaseconfig)


# db = firebase.database()
# firebase = pyrebase.initialize_app(firebaseconfig)
# authe = firebase.auth()


def directHome(request):
    return render(request, "test.html")


def complaintFront(request):
    return render(request, "complaint1front.html")


def complaintReply(request):
    return render(request, "complaint2Reply.html")


def complaintTyping(request):
    return render(request, "complaint3Type.html")


def complaintCheckReply(request):
    return render(request, "complaint4CheckReply.html")


def complaintUpdateReply(request):
    return render(request, "complaint5Update.html")


def complaintView(request):
    return render(request, "complaint6View.html")


def addExpenses(request):
    return render(request, "AddExpense1.html")


def Expenseslist(request):
    return render(request, "ExpensesList.html")


def AddRevenue(request):
    return render(request, "AddRevenue3.html")


def RevenueList(request):
    return render(request, "RevenueList4.html")


def Capital(request):
    return render(request, "CapitalAccount5.html")


def update6(request):
    return render(request, "update.html")

def ledgers(request):
    return render(request, "Ledgers7.html")


def ledgersView(request):
    return render(request, "ViewLedgers8.html")


def reports9(request):
    return render(request, "Reports.html")


def reportsdisplay(request):
    return render(request, "ReportsDisplay.html")

def directaddsupplier(request):
    return render(request, "addSupplier.html")


def directaddstock(request):
    return render(request, "addStock.html")


def directinventory(request):
    return render(request, "inventory.html")


def directpurchaseOrders(request):
    return render(request, "purchaseOrders.html")


def directsuppliers(request):
    return render(request, "suppliers.html")


def directcreatecustomergroups(request):
    return render(request, "createCustomerGroups.html")


def custloign(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    authe = firebase.auth()
    email = request.POST.get('email')
    pwd = request.POST.get('pwd')
    print(email)
    print(pwd)
    try:
        user = authe.sign_in_with_email_and_password(email, pwd)
    except:
        message = "Invalid username or password please try again"
        return render(request, "customerlogin.html", {"msg": message})
    print(user['idToken'])
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, "test.html")


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(request('customerlogin.html'))


def addAdditionalDeductions(request):
    return render(request, "addAdditionalDeductions.html")


def addEarnings(request):
    return render(request, "addAdditionalEarnings.html")


def additionsDeductions(request):
    return render(request, "AdditionsDeductions.html")


def EPFOfWhoseSalaryIsNeeded(request):
    return render(request, "EPFOfWhoseSalaryIsNeeded.html")


def EPFToCalculateSalary(request):
    return render(request, "EPFToCalculateSalary.html")


def directPayrollManagementHome(request):
    return render(request, "PayrollManagementHome.html")


def dirPaySlip(request):
    return render(request, "PaySlip.html")


def dirSalaryDetailsOfAllEmployees(request):
    return render(request, "SalaryDetailsOfAllEmployees.html")


def dirSalaryHistoryOfEmployee(request):
    return render(request, "SalaryHistoryOfEmployee.html")


def dirUpdateAdditionsOrDeductions(request):
    return render(request, "UpdateAdditionsOrDeductions.html")


def dirContinuousReport(request):
    return render(request, "continuousReport.html")


def dirHousekeepingReport(request):
    return render(request, "HousekeepingReport.html")


def dirInsertRoomDetails(request):
    return render(request, "InsertRoomDetails.html")


def dirRoomDetails(request):
    return render(request, "roomDetails.html")


def dirRoomManagementHome(request):
    return render(request, "RoomManagementHome.html")


def dirUpdateRoomDetails(request):
    return render(request, "UpdateRoomDetails.html")

def loadaddmeal(request):
    return render(request,"addmeal.html")
def InsertRooms(request):
    return render(request, "roomDetails.html")

def addmeal(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    mealname = request.POST.get('name')
    price = request.POST.get('price')
    spice = request.POST.get('spicelvl')
    desc = request.POST.get('desc')
    veg = request.POST.get('veg')
    data = {"price": price, "spicelvl": spice, "desc": desc, "veg": veg}
    db.child("resturant").child("meals").child(mealname).set(data)
    return render(request, "test.html")


def addbeverage(request):
    return render(request, "addbeverage.html")


def loadupdatemeal(request):
    return render(request, "updatemeal.html")

def getmeals(request, firebase=None):
    firebase = firebase.FirebaseApplication('https://theoceancolombo-c128a.firebaseio.com/resturant')
    result = firebase.get('meals', None)
    print(result)


def updatemeal(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    mealname = request.POST.get('name')
    price = request.POST.get('price')
    desc = request.POST.get('desc')
    spice = request.POST.get('spicelvl')
    veg = request.POST.get('veg')
    data = {"price": price, "spicelvl": spice, "desc": desc, "veg": veg}
    db.child("resturant").child("meals").child(mealname).update(data)
    getdata = db.child("resturant").child("meals").get()
    for task in getdata.each():
        print(task.val())
        print(task.key())
    return render(request, "test.html")

def updatebeverage(request):
    return render(request, "updatebeverage.html")

def bookvhecicale(request):
    return render(request,"BookVehicle.html")
def mealmngt(request):
    return render(request, "resturantmealmngt.html")

def custbillhistory(request):
    return render(request, "poscustbillhistory.html")

def loadcustpos(request):
    return render(request,"poscustomer.html")

def selectroom(request):
    return render(request, 'selectRoom.html')


def loadselectroom(request):
    return render(request, 'selectroom.html')


def confirmbooking(request):
    return render(request, 'confirmBooking.html')


def loadconfirmbooking(request):
    return render(request, 'confirmBooking.html')


def cancelbooking(request):
    return render(request, 'cancelBooking.html')


def loadcancelbooking(request):
    return render(request, 'cancelBooking.html')


def updatebooking(request):
    return render(request, 'updateBooking.html')


def loadupdatebooking(request):
    return render(request, 'updateBooking.html')
