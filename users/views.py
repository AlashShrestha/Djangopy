from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmpassword = request.POST.get("confirmpassword")

        if password == confirmpassword:
            users = User.objects.create_user(
                username=username,
                first_name=firstname,
                last_name=lastname,
                email=email,
                password=password,
            )
            # users.set_password(password)
            users.save()
        return redirect("crud:home")
    return render(request, "register.html")


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("crud:home")
        else:
            return redirect("users:login")
    return render(request, "login.html")


@login_required
def logoutUser(request):
    logout(request)
    return redirect("crud:home")


def forgotpassword(request):
    if(request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirmpassword = request.POST.get("confirmpassword")
        if(password == confirmpassword):
            user = User.objects.get(username=username)
            if(user):
                user.set_password(password) 
                user.save()      
        return redirect("users:forgot")