from django.urls import path
from users.views import *

app_name = "users"
urlpatterns = [
    path("register/", register, name="register"),
    path("login/", loginUser, name="login"),
    path("logout/", logoutUser, name="logout"),
    path("forgot/", forgotpassword, name="forgot"),
]
