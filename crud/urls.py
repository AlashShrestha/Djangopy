from django.urls import path

from crud.views import *

urlpatterns = [
    path("", home, name='home'),
    path("index/", index, name='index'),
    path("about/", about, name='about'),
    path("create/", create, name='create'),
    path("contact/", contact, name='contact'),
    path("<int:id>/", partData, name='partData'),
    path('delete/<int:id>/', deleteBlog, name='deleteBlog'),
    path('update/<int:id>/', updateBlog, name='updateBlog'),
]
