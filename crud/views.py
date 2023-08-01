from multiprocessing import context
from turtle import title
from django.shortcuts import redirect, render
from .models import Blog, Contact
from datetime import date
from crud.forms import BlogForm

# Create your views here.
def home(request):
    blog = Blog.objects.all()
    if (request.method == "POST"):
        searchData = request.POST.get("search")
        if (searchData != ""):
            data = Blog.objects.filter(title__icontains = searchData)
            return render(request, "blog/home.html", {"blogs": data})
    return render(request, "blog/home.html", {"blogs": blog})


def create(request):
    if request.method == "POST":
        data_user_name = request.POST.get("user_name")
        data_title = request.POST.get("title")
        data_sub_heading = request.POST.get("sub_heading")
        data_content = request.POST.get("content")
        blog = Blog(
            user_name=data_user_name,
            title=data_title,
            sub_heading=data_sub_heading,
            content=data_content,
            date=date.today(),
        )
        blog.save()
        return redirect("crud:home")
    return render(request, "blog/create.html")


def about(request):
    return render(request, "blog/about.html")


def contact(request):
    if request.method == "POST":
        data_name = request.POST.get("name")
        data_email = request.POST.get("email")
        data_phone = request.POST.get("phone")
        data_message = request.POST.get("message")
        contact = Contact(
            user_name=data_name,
            title=data_email,
            phone=data_phone,
            message=data_message,
        )
        contact.save()
        return redirect("crud:home")
    return render(request, "blog/contact.html")


def post(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, "blog/post.html", {"blog": blog})

def deletBlog(request, id):
    blogs = Blog.objects.get(id=id)
    blogs.delete()
    return redirect('crud:home')


def updateBlog(request, id):
    blog = Blog.objects.get(id=id)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect("crud:create")
    context = {
        'form': form,
        'user_name': blog.user_name,
        'title' : blog.title,
        'sub_heading' : blog.sub_heading,
        'content' : blog.content,
    }
    return render(request, "blog/create.html", context)

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


