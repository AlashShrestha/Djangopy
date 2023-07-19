from django.shortcuts import redirect, render
from .models import Blog, Contact
from .forms import BlogForm

# Create your views here.
def index(request):
    blog = Blog.objects.all()
    return render(request, "index.html", {"blogs": blog})


def about(request):
    return render(request, "about.html")


def create(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, "create.html", {"forms": form})


def contact(request):
    if(request.method == "POST"):
        dataName = request.POST.get("name")
        dataEmail = request.POST.get("email")
        contact = Contact(
            name = dataName,
            email = dataEmail
        )
        contact.save()
    return render(request, "contact.html")


def partData(request, id):
    blog = Blog.objects.get(id = id)
    context = {
        "blog": blog
        }
    return render(request, "index.html", context)