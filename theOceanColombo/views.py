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






