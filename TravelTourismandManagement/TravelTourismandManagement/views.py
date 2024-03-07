from django.shortcuts import render

def homePage(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")
def gallery(request):
    return render(request, "gallery.html")
def login(request):
    return render(request, "login.html")
def home(request):
    return render(request, "home.html")
def registrationPage(request):
    return render(request, "register.html")