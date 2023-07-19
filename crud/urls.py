from django.urls import path

from crud.views import index, about, create, contact, partData

urlpatterns = [
    path("", index, name='index'),
    path("about/", about, name='about'),
    path("create/", create, name='create'),
    path("contact/", contact, name='contact'),
    path("<int:id>/", partData, name='partData'),
]
