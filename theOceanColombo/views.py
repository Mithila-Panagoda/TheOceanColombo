from django.http import HttpResponseRedirect
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

#firebase = pyrebase.initialize_app(config)


#authe = firebase.auth()


def directHome(request):
    return render(request, "test.html")


def complaintFront(request):
    return render(request, "complaint1front.html")
def complaintFrontdata(request):
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    name = request.POST.get('cusname')
    email = request.POST.get('email')
    phnNo = request.POST.get('phn')
    feed = request.POST.get('feed')
    data = {"Name": name, "Email": email, "phnNumber": phnNo, "Feed": feed}
    db.child("Complaint").child("customerFeedback").child(name).set(data)
    return render(request, "complaint2Reply.html")

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

def addExpensesACC(request):
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    id = request.POST.get('id1')
    date = request.POST.get('date1')
    price = request.POST.get('price1')
    description = request.POST.get('des1')

    data = {"Date": date, "Price": price, "Description": description}
    db.child("Accounts").child("expenses").child(id).set(data)
    return render(request, "ExpensesList.html")

def Expenseslist(request):
    return render(request, "ExpensesList.html")

def AddRevenue(request):
    return render(request, "AddRevenue3.html")
def AddRevenueAcc(request):
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    id = request.POST.get('revId')
    date = request.POST.get('revDate')
    price = request.POST.get('revPrice')
    description = request.POST.get('revDis')
    data = {"Date": date, "Price": price, "Description": description}
    db.child("Accounts").child("Revenue").child(id).set(data)
    return render(request, "RevenueList4.html")




def RevenueList(request):
    return render(request, "RevenueList4.html")

def Capital(request):
    return render(request, "CapitalAccount5.html")
def CapitalAcc(request):
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    id = request.POST.get('capId')
    date = request.POST.get('capDate')
    type = request.POST.get('capType')
    price = request.POST.get('capPrice')
    description = request.POST.get('capDes')

    data = {"Date": date, "Price": price, "Description": description, "Type": type}
    db.child("Accounts").child("CapitalAccount").child(id).set(data)
    return render(request, "ViewCapital.html")

def ViewCapital(request):
    return render(request, "ViewCapital.html")


def update6(request):
    return render(request, "updateTransacktion.html")

def ledgers(request):
    return render(request, "Ledgers7.html")

def ledgersView(request):
    return render(request, "ViewLedgers8.html")

def reports9(request):
    return render(request, "ExpensesReports.html")

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

