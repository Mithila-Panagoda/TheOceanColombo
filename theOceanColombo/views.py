from django.shortcuts import render
import pyrebase

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
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()


def directHome(request):
    return render(request, "test.html")

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


