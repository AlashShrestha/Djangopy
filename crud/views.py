from django.shortcuts import redirect, render
from .models import Blog, Contact
from .forms import BlogForm

# Create your views here.
def index(request):
    blog = Blog.objects.all()
    return render(request, "index.html", {"blogs": blog})

def home(request):
    return render(request, "blog/home.html",)

def about(request):
    return render(request, "blog/about.html")

def contact(request):
    return render(request, "blog/contact.html")

def create(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, "create.html", {"forms": form})


# def contact(request):
#     if(request.method == "POST"):
#         dataName = request.POST.get("name")
#         dataEmail = request.POST.get("email")
#         contact = Contact(
#             name = dataName,
#             email = dataEmail
#         )
#         contact.save()
#         return redirect('index')
#     return render(request, "contact.html")


def partData(request, id):
    blog = Blog.objects.get(id = id)
    context = {
        "blog": blog
        }
    return render(request, "index.html", context)

def deleteBlog(request, id):
    blog = Blog.objects.get(id = id)
    blog.delete()
    return redirect('index')

def updateBlog(request, id):
    blog = Blog.objects.get(id = id)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, 'create.html', {'forms': form})
