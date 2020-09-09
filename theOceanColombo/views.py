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

# firebase = pyrebase.initialize_app(config)

# authe = firebase.auth()

#authe = firebase.auth()

authe = firebase.auth()

firebase = pyrebase.initialize_app(firebaseconfig)


# db = firebase.database()
# firebase = pyrebase.initialize_app(firebaseconfig)
# authe = firebase.auth()

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

def Expenseslist(request):
    return render(request, "ExpensesList.html")

def AddRevenue(request):
    return render(request, "AddRevenue3.html")

def RevenueList(request):
    return render(request, "RevenueList4.html")

def Capital(request):
    return render(request, "CapitalAccount5.html")

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

def roomDetails(request):
    db = firebase.database()
    #rooms = db.child("Rooms").get()
    #print(rooms.val())
    return render(request, 'roomDetails.html', {'content': db.child("Rooms").get()})

def dirRoomManagementHome(request):
    return render(request, "RoomManagementHome.html")


def dirUpdateRoomDetails(request):
    return render(request, "UpdateRoomDetails.html")

def loadaddmeal(request):

    return render(request, "addmeal.html")
def InsertRooms(request):
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    roomNo = request.POST.get('roomNumber')
    roomType = request.POST.get('roomType')
    description = request.POST.get('description')
    roomImage = request.POST.get('image')

    #push data
    data = {"Room Number" : roomNo, "Room Type" : roomType, "Description" : description, "Room Image" : roomImage}
    db.child("Rooms").child(roomNo).set(data)
    return render(request, "InsertRoomDetails.html")

def addmeal(request):
    return render(request, "addmeal.html")

def addbeverage(request):
    return render(request, "addbeverage.html")

def updatemeal(request):
    return render(request, "updatemeal.html")
  
def updatebeverage(request):
    return render(request, "updatebeverage.html")


def dirBackendHome(request):
    return render(request, "BackendHome.html")

def checkDetails(request):
    db = firebase.database()
    timestamps = db.child('Rooms').shallow().get().val()
    lis_time = []

    for i in timestamps:
        lis_time.append(i)
        lis_time.sort(reverse = True)
    print(lis_time)

    work = []

    for i in lis_time:
        wor = db.child('Rooms').child(i).get().val().values()
        work.append(wor)

    print(work)

    comb_list = zip(lis_time, work)

    return render(request, "roomDetails.html", {'comb_list':comb_list})
  
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
    return render(request, "resturantmealmngt.html")
def loadaddbeverage(request):
    return render(request, "addbeverage.html")
def addbeverage(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    name = request.POST.get('name')
    price = request.POST.get('price')
    size = request.POST.get('size')
    desc = request.POST.get('desc')
    type = request.POST.get('drink')
    data={"price":price,"size":size,"desc":desc,"type":type }
    db.child("resturant").child("beverages").child(name).set(data)
    return render(request, "resturantmealmngt.html")

def loadupdatebeverage(request):
    return render(request,"updatebeverage.html")
def updatebeverage(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    name = request.POST.get('name')
    price = request.POST.get('price')
    size = request.POST.get('size')
    desc = request.POST.get('desc')
    drink = request.POST.get('drink')
    data={"price":price,"size":size,"desc":desc,"drink":drink}
    db.child("resturant").child("beverages").child(name).update(data)
    return render(request, "resturantmealmngt.html")

def bookvhecicale(request):
    return render(request,"BookVehicle.html")
def mealmngt(request):
    #getting meals and loading to html page
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    data=db.child("resturant").child("meals").get()
    to=data.val()
    print(data.val())
    return render(request, "resturantmealmngt.html",)

def custbillhistory(request):
    return render(request, "poscustbillhistory.html",)

def Newemployee(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    First_Name = request.POST.get('firstName')
    Last_Name = request.POST.get('lastName')
    NIC = request.POST.get('NIC')
    Title = request.POST.get('Title')
    Employment_type = request.POST.get('employeeType')
    Email = request.POST.get('Email')
    Address = request.POST.get('Address')
    Phone = request.POST.get('Phone')
    EPF = request.POST.get('EPF')
    Emergency_Contact= request.POST.get('EmergencyCon')
    data = {"firstName": First_Name, "lastName": Last_Name, "NIC": NIC, "Title": Title,"employeeType": Employment_type,
            "Email": Email, "Address": Address, "Phone":Phone,"EmergencyCon":Emergency_Contact}
    db.child("Staff").child("Employee").child(EPF).set(data)
    return render(request, "ViewEmployee.html")

def loadNewemployee(request):
    return render(request, "NewEmployee.html")

def Viewemployee(request):
    return render(request, "ViewEmployee.html")

def loadViewemployee(request):
    return render(request, "ViewEmployee.html")

def Promomanagement(request):
    return render(request, "PromoManagement.html")

def loadPromomanagement(request):
    return render(request, "PromoManagement.html")

def Updatepromo (request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    EPF = request.POST.get('EPF')
    First_Name= request.POST.get('firstName')
    Title = request.POST.get('Title')
    data = {"firstName": First_Name, "Title": Title}
    db.child("Staff").child("Employee").child(EPF).update(data)
    return render(request, "PromoManagement.html")

def loadUpdatepromo (request):
    return render(request, "UpdatePromo.html")
  
def loadcustpos(request):
    return render(request,"poscustomer.html")

def addcustbill(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    cname = request.POST.get('cname')
    nic = request.POST.get('nic')
    rtype = request.POST.get('rtype')
    rcharge = request.POST.get('rcharge')
    resturantfee = request.POST.get('resturantfee')
    addcharge = request.POST.get('addcharge')
    ptype = request.POST.get('ptype')
    tax = request.POST.get('tax')
    date = request.POST.get('date')
    data={"Name":cname,"RoomType":rtype,"roomCharge":rcharge,"resturantFee":resturantfee,"addcharge":addcharge,"paymentType":ptype,"TAX":tax}
    db.child("POS").child("customerbills").child(nic).child(date).set(data)
    return render(request,"test.html")

def loadresturantposhome(request):
    return render(request,"resturantpostblselection.html")

def custreg(request):
    return render(request, "customerRegistration.html")

def loadcustreg(request):
    return render(request, "customerRegistration.html")

def attendance(request):
    return render(request, "attendance.html")

def loadattendance(request):
    return render(request, "attendance.html")

def search(request):
    return render(request, "search.html")

def loadsearch(request):
    return render(request, "search.html")

def searchresults(request):
    return render(request, "searchResults")

def loadsearchresults(request):
    return render(request, "searchResults")

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


def loadupdatebooking(request):
    return render(request, 'updateBooking.html')

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
