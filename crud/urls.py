from django.urls import path

from crud.views import *

urlpatterns = [
    path("", index),
    path("about/", about)
]
