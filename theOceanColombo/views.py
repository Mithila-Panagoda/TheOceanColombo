from django.shortcuts import render
import pyrebase
from django.contrib import auth

config = {
    'apiKey': "AIzaSyBew42hA7iZHy7zs47WMqIg-GSBnxP-ttM",
    'authDomain': "theoceancolombo-c128a.firebaseapp.com",
    'databaseURL': "https://theoceancolombo-c128a.firebaseio.com",
    'projectId': "theoceancolombo-c128a",
    'storageBucket': "theoceancolombo-c128a.appspot.com",
    'messagingSenderId': "925636680144",
    'appId': "1:925636680144:web:da1ab5d4f3b0d3231b01d5",
    'measurementId': "G-YH7TV23J8J"
}


# firebase = pyrebase.initialize_app(config)

# authe = firebase.auth()


def directHome(request):
    return render(request, "test.html")


def directaddsupplier(request):
    return render(request, "addSupplier.html")


def addsupplier(request):
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    supplierid = request.POST.get('SupplierId')
    suppliername = request.POST.get('SupplierName')
    nic = request.POST.get('nic')
    registeredno = request.POST.get('registeredno')
    email = request.POST.get('email')
    address = request.POST.get('address')

    data = {"Suppliername": suppliername, "nic": nic, "Registeredno": registeredno, "Email": email, "Address": address}
    db.child("Supplier").child(supplierid).set(data)
    return render(request, "suppliers.html")


def directmessages(request):
    return render(request, "Messages.html")

def addmessages(request):
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    messageid = request.POST.get('messageId')
    message = request.POST.get('message')

    data={"message":message}
    db.child("Messages").child(messageid).set(data)
    return render(request,"Messages.html")

def sendmessages(request):
    return render(request, "SendMessages.html")

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
    return request(request, "test.html")


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
