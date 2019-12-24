from django.shortcuts import render,redirect
from django.contrib import messages
from b_admin.smssending import sendSMS
from user.models import UserModel



def Admincheck(request):
    username=request.POST['a1']
    password=request.POST['a2']
    if username == "admin" and password == "admin143":
        return render(request,"b_admin template/adminhome.html")
    else:
        messages.error(request,"invalid details")
        return redirect("b_admin")


def Pending_reg(request):
    qs=UserModel.objects.filter(status="pending")

    return render(request,"b_admin template/pending.html",{"data":qs})


def approved_reg(request):
    qs = UserModel.objects.filter(status="approved")
    return render(request,"b_admin template/approve_reg.html",{"data":qs})


def decline_reg(request):
    qs = UserModel.objects.filter(status="declined")
    return render(request, "b_admin template/decline_reg.html", {"data": qs})


def approved(request):
    idno=request.POST['a1']
    qs=UserModel.objects.filter(id=idno)
    name=""
    contact=""

    for x in qs:
        name=x.name
        contact=x.contact
    qs.update(status="approved")
    print(name)
    print(contact)
    message="hi,"+name+"  approved by admin and you can login with your credentials"
    x=sendSMS(str(contact),message)
    print(x)
    return redirect("approved_reg")


def declined(request):
    idno=request.POST['d1']
    qs=UserModel.objects.filter(id=idno)
    name=""
    contact=""
    for x in qs:
        name=x.name
        contact=x.contact
    qs.update(status="declined")
    message="hi,"+name+" admin declined you and you are not able to login to this site "
    x=sendSMS(str(contact),message)
    print(x)

    return redirect("decline_reg")


def logout(request):
    return redirect("home")
