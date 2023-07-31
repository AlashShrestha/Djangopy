from django.urls import path

from crud.views import *

app_name = "crud"
urlpatterns = [
    path("", home, name="home"),
    path("create/", create, name="create"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("post/<int:id>/", post, name="post"),
    # path("post/", create, name="post"),
    # path("delete/<int:id>/", deleteBlog, name="deleteBlog"),
    # path("update/<int:id>/", updateBlog, name="updateBlog"),
]
