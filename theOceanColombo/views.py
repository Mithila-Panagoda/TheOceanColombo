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
