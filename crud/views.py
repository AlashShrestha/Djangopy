from django.shortcuts import render
from crud.models import Blog

# Create your views here.
def index(request):
    blog = Blog.objects.all()
    return render(request, "index.html", {"blogs": blog})


def about(request):
    return render(request, "about.html")
