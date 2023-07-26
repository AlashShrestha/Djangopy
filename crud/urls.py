from django.urls import path

from crud.views import *

app_name = "crud"
urlpatterns = [
    path("", home, name="home"),
    path("post/", post, name="post"),
    path("about/", about, name="about"),
    path("create/", create, name="create"),
    path("contact/", contact, name="contact"),
    path("post/<int:id>/", partData, name="partData"),
    # path("delete/<int:id>/", deleteBlog, name="deleteBlog"),
    # path("update/<int:id>/", updateBlog, name="updateBlog"),
]
