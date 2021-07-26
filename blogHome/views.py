from django.http import request
from django.shortcuts import render,HttpResponse
from blogHome.models import Blog, Contact
import math
def home(response):
    return render(response,'index.html')

def blog(request):

    no_of_post = 3
    page = request.GET.get('page')
    if page is None:
        page = 1
        print(page)
    else:
        page = int(page)    
        print(page)

    blogs = Blog.objects.all()
    length = len(blogs)
    blogs = blogs[(page-1)*no_of_post : page*no_of_post]
    if page > 1:
        prev = page-1
    else:
        prev = None
    if page < math.ceil(length/no_of_post):
        nxt = page + 1
    else:
        nxt = None

    context = {'blogs': blogs,'prev': prev,'nxt': nxt}
    return render(request,'blog.html',context)

def blogpost(response,slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog': blog}
    return render(response,'blogpost.html',context)

def search(response):
    return render(response,'search.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        instance = Contact(name=name,email=email,phone=phone,desc=desc)
        instance.save()
    return render(request,'contact.html')

# Create your views here.
