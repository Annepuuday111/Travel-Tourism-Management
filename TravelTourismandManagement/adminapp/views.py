from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Admin, Register
from django.contrib import messages
from .models import Packages
#from .forms import PackageForm

def checkadminlogin(request):
    if request.method == "POST":
        uname = request.POST["uname"]  # gets username
        pwd = request.POST["pwd"]
        flag=0
        flag = Register.objects.filter(username=uname, password=pwd).values()
        print("flag = ",flag)
        if flag:
            if uname == "Mohan":
                messages.info(request, "Welcome Admin..!")
                return render(request, "adminhome.html")
        if flag:
            messages.info(request, "This is Users Home Page..!")
            return render(request, "home.html")
        else:
            return render(request, "loginfail.html")

def checkregistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        addr = request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]

        if pwd == cpwd:
            if Register.objects.filter(username=uname).exists():
                messages.info(request, "username taken...")
                return render(request, "register.html")
            elif Register.objects.filter(email=email).exists():
                messages.info(request, "email taken...")
                return render(request, "register.html")
            else:
                user = Register.objects.create(name=name,address=addr, email=email, phno=phno,username=uname,password=pwd)
                user.save()
                messages.info(request, "user created...")
                return render(request, "login.html")
        else:
            messages.info(request, "password is not matching...")
            return render(request, "register.html")

def checkpackages(request):
    if request.method == "POST":
        tcode = request.POST["tourcode"]   #request.method is used to get the data from HTML
        tname = request.POST["tourname"]
        tpack = request.POST["tourpackage"]
        tdesc = request.POST["desc"]
        pack = Packages.objects.create(tourcode=tcode, tourname=tname, tourpackage=tpack, desc=tdesc)
        pack.save()
        messages.info(request, "Data Inserted Successfully")
        return render(request, "package.html")
    else:
            return render(request, "package.html")

def viewplaces(request):
    data = Packages.objects.all()
    return render(request,"viewplaces.html",{"placesdata":data})
