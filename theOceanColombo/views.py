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


