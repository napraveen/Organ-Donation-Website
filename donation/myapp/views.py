from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Person
# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method =='POST':
        username= request.POST['username']
        password= request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if username =="admin":
                return redirect('donors')
            return redirect('donate')
        else:
            messages.info(request, 'Credential Invalid')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method =='POST':
        username = request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2 = request.POST['password2']
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Username already Exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info("Password not the same")
            return redirect('register')

    else:
        return render(request,'register.html')

def new(request):
    if request.method=="POST":
        username = request.POST["username"]
        name = request.POST["name"]
        mobile = request.POST["mobileno"]
        email = request.POST["email"]
        city = request.POST["city"]
        gender = request.POST["gender"]
        organ_pledged = request.POST["organpl"]
        blood_group = request.POST["bloodgr"]
        if len(str(mobile)) != 10:
            return redirect('new')
        new_person = Person(username=username, name=name, mobile=mobile, email=email, city=city,gender=gender, organ_pledged=organ_pledged, blood_group=blood_group)
        new_person.save()
        return redirect('certificate')
    return render(request,'new.html')

def donors(request):
    persons = Person.objects.all()
    return render(request,'donors.html',{"persons":persons})

def certificate(request):
    persons = Person.objects.all()
    return render(request, 'certificate.html',{"persons":persons})

def donate(request):
    return render(request,'donate.html')

def dummy(request):
    persons = Person.objects.all()
    return render(request,'dummy.html',{"persons":persons})

def donors2(request):
    persons = Person.objects.all()
    return render(request,'donors2.html',{"persons":persons})

def about(request):
    return render(request, 'about.html')

# def delete(request,id):
#     member = Person.objects.get(id=id)
#     member.delete()
#     return redirect('donors')

def add(request,id):
    my_list = []
    member = Person.objects.get(id=id)
    my_list.append(member)
    members = Person.objects.all()
    return render(request,'donors.html',{'members':members})