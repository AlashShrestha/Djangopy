from django.shortcuts import redirect, render
from .models import Blog
from .forms import BlogForm


# Create your views here.
def home(request):
    return render(request, "blog/home.html")


def post(request):
    blog = Blog.objects.all()
    context = {"blogs": blog}
    return render(request, "post.html", context)


def about(request):
    return render(request, "blog/about.html")


def contact(request):
    return render(request, "blog/contact.html")


def create(request):
    return render(request, "blog/create.html")


# def create(request):
#     form = BlogForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect("post")
#     return render(request, "create.html", {"forms": form})


# def contact(request):
#     if(request.method == "POST"):
#         dataName = request.POST.get("name")
#         dataEmail = request.POST.get("email")
#         contact = Contact(
#             name = dataName,
#             email = dataEmail
#         )
#         contact.save()
#         return redirect('post')
#     return render(request, "contact.html")


def partData(request, id):
    blog = Blog.objects.get(id=id)
    context = {"blog": blog}
    return render(request, "post.html", context)


# def deleteBlog(request, id):
#     blog = Blog.objects.get(id=id)
#     blog.delete()
#     return redirect("post")


# def updateBlog(request, id):
#     blog = Blog.objects.get(id=id)
#     form = BlogForm(request.POST or None, instance=blog)
#     if form.is_valid():
#         form.save()
#         return redirect("post")
#     return render(request, "create.html", {"forms": form})
