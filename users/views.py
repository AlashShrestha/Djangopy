from django.shortcuts import redirect, render
from django.contrib.auth.models import User


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
                firstname=firstname,
                lastname=lastname,
                email=email,
            )
            users.set_password(password)
            users.save()
        return redirect("crud:home")
    return render(request, "register.html")
