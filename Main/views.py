from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm, AuthForm, AddForm
from .models import User, Image
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    return render(request, "index.html")

def about(request):
    return  render(request, "about1.ejs")

def index2(request):
    return render(request, "index.ejs")

def game(request):
    return render(request, "game.ejs")

def support(request):
    return render(request, "support.ejs")
    
def collection(request):
    arts=Image.objects.all()
    paginator=Paginator(arts, 5)
    # pages = Paginator.page(1)
    context={
        "arts":arts,
        # "pages":pages
    }
    return render(request, "collection.ejs", context)

def sign_in(request):
    if request.method=='POST':
        user=User()
        user.nickname=request.POST.get('nickname')
        user.age=request.POST.get('age')
        user.mail=request.POST.get('mail')
        user.password=make_password(request.POST.get('password'))
        user.save()
        return render(request, "reqsuc.html")
    else:
        form=UserForm()
        return render(request, "reg.html")

def auth(request):
    if request.method=='POST':
        form=AuthForm(request.POST)
        if form.is_valid():
            usr=User.objects.get(mail=request.POST.get('mail'))
            if usr:
                pas=check_password(request.POST.get('password'), usr.password)
                if pas:
                    # data={"nickname":usr.nickname, "id":usr.id_user}
                    return render(request, 'auth_suc.html', context={"data":usr.nickname, "dt":usr.id_user, 'usr':usr})
                else:
                    return HttpResponse('failed authorization')
        else: return HttpResponse('bad request')
    else:
        form=AuthForm()
        return render(request,'auth.html')

def logout(request):
    return render(request, 'logout.html')

def addArt(request):
    if request.method=='POST'  and request.FILES:
        form=AddForm(request.POST)
        # if form.is_valid():
        art=Image()
        art.name=request.POST.get('artname')
        art.img=request.FILES['art']
        art.teg1=request.POST.get('tag1')
        art.teg2=request.POST.get('tag2')
        art.teg3=request.POST.get('tag3')
        art.teg4=request.POST.get('tag4')
        art.teg5=request.POST.get('tag5')
        art.author=request.POST.get('author')
        art.author1=(request.POST.get('author1'))
        art.save()
        print (request.user)
        return render(request, "add_suc.html")
        # else: return HttpResponse(request)
    else:
        form=AddForm()
        return render(request, 'addArt.html')