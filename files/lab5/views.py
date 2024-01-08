from django.shortcuts import render
from django.contrib.auth import logout

def login_view(request):
    if request.method == "GET":
        return render(request, "login/login.html")
