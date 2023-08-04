from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .models import Blog, Contact, Links, CompanyName
from datetime import date
from crud.forms import BlogForm
from Demo.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


# Create your views here.
def home(request):
    blog = Blog.objects.all()
    paginator = Paginator(blog, 2)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    link = Links.objects.all()
    company_name = CompanyName.objects.all()[0]
    context = {
        "blogs": page_obj,
        "links": link,
        "company_name": company_name.name,
    }
    if request.method == "POST":
        searchData = request.POST.get("search")
        if searchData != "":
            data = Blog.objects.filter(title__icontains=searchData)
            return render(request, "blog/home.html", {"blogs": data})
    return render(request, "blog/home.html", context)


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
    link = Links.objects.all()
    company_name = CompanyName.objects.all()[0]
    context = {"links": link, "company_name": company_name.name}
    return render(request, "blog/create.html", context)


def about(request):
    link = Links.objects.all()
    company_name = CompanyName.objects.all()[0]
    context = {"links": link, "company_name": company_name.name}
    return render(request, "blog/about.html", context)


def contact(request):
    link = Links.objects.all()
    company_name = CompanyName.objects.all()[0]
    context = {"links": link, "company_name": company_name.name}
    if request.method != "POST":
        return render(request, "blog/contact.html", context)
    data_name = request.POST.get("name")
    data_email = request.POST.get("email")
    data_message = request.POST.get("message")
    data_subject = "Django Email"
    recipient = ("kajullenneupri-3691@yopmail.com",)
    contact = Contact(
        name=data_name,
        email=data_email,
        message=data_message,
    )
    contact.save()
    template = render_to_string(
        "blog/email.html",
        {"name": data_name, "description": data_message, "mail": data_email},
    )
    email = EmailMessage(
        data_subject,
        template,
        EMAIL_HOST_USER,
        recipient,
    )
    email.fail_silently = False  # type: ignore
    if email != None:
        email.send()
    return redirect("crud:contact")


def post(request, id):
    blog = Blog.objects.get(id=id)
    link = Links.objects.all()
    company_name = CompanyName.objects.all()[0]
    context = {"blog": blog, "links": link, "company_name": company_name.name}
    return render(request, "blog/post.html", context)


def deletBlog(request, id):
    blogs = Blog.objects.get(id=id)
    blogs.delete()
    return redirect("crud:home")


def updateBlog(request, id):
    blog = Blog.objects.get(id=id)
    form = BlogForm(request.POST or None, instance=blog)
    link = Links.objects.all()
    company_name = CompanyName.objects.all()[0]
    if form.is_valid():
        form.save()
        return redirect("crud:create")
    context = {
        "form": form,
        "user_name": blog.user_name,
        "title": blog.title,
        "sub_heading": blog.sub_heading,
        "content": blog.content,
        "links": link,
        "company_name": company_name.name,
    }
    return render(request, "blog/create.html", context)


def footer(request):
    link = Links.objects.all()
    company_name = CompanyName.objects.all()[0]
    context = {"links": link, "company_name": company_name.name}
    print(link, company_name)
    return render(request, "footer.html", context)


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
