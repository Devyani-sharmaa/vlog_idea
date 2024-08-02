
from django.shortcuts import render,redirect
from django.http import HttpResponse
from cartoon.models import contactMe
# Create your views here.
def myhome(request):
   # return HttpResponse("this is my first url hit")
    return render(request,"home.html")

def about(request):
   # return HttpResponse("THIS IS ABOUT PAGE ")
    return render(request,"about.html")

def service(request):
    x=contactMe.objects.all()
    print(x)
    return render(request,"services.html",{"hi":x})

 

def contact(request):
    return render(request,"contact.html")


def savedata(request):
    if request.method=="POST":
        name=request.POST.get("fname")
        email=request.POST.get("email")
        phone_no=request.POST.get("phn")
        message=request.POST.get("msg")
        print(name,email,message)
        data=contactMe(fname=name,email=email,msg=message)
        data.save("x")

    return redirect('x')

    return HttpResponse("DATA IS SAVA SUCESS")

def deletefata(request, x):
    q = contactMe.objects.get(id = x)
    q.delete()
    return redirect('p')

    # return HttpResponse("DATA IS delete SUCESS")
    # pass


def updatedata(request,bb): 
    obj=contactMe.objects.get(id=bb)
    return render(request,"updatedata.html",{"record":obj})
    return redirect("p")


def datarecord(request,bb):
    obj=contactMe.objects.get(id=bb)
    if request.method=="POST":
        name=request.POST.get("fname")
        email=request.POST.get("email")
        phone_no=request.POST.get("phn")
        message=request.POST.get("msg")

        obj.fname=name
        obj.email=email
        obj.phn=phone_no
        obj.msg=message

        obj.save()
    return redirect("p")
#blog----home,about,contact,services