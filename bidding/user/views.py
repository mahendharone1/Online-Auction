from django.shortcuts import render, redirect
from user.models import UserModel, ProductModel,BidTable
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def Savereg(request):
    name = request.POST['r1']
    contact = request.POST['r2']
    email = request.POST['r3']
    password = request.POST['r4']
    status = "pending"
    us = UserModel(name=name, contact=contact, email=email, password=password, status=status)
    us.save()
    messages.error(request, "Admin need to approve your request thank you for register withus")

    return redirect("reg")


def login_data(request):
    contact = request.POST['l1']
    password = request.POST['l2']
    try:
        result = UserModel.objects.get(contact=contact, password=password)
        print(contact, password)
        print(result.contact, result.password)
        print(result.status)
    except UserModel.DoesNotExist:
        messages.error(request, "Invalid User")
        return redirect("Buyer_Seller")
    if result.status == "approved":
        request.session['user_name'] = result.name
        request.session['user_id'] = result.id
        return render(request, "user templates/user_home.html")
    elif result.status == "pending":
        messages.error(request, "request is pending")
        return redirect("Buyer_Seller")
    else:
        messages.error(request, "request is decline")
        return redirect("Buyer_Seller")
    return redirect("Buyer_Seller")


def user_logout(request):
    try:
        del request.session["user_name"]
    except KeyError:
        messages.error(request, "")
    return redirect("home")


def user_seller(request):
    try:
        u=request.session["user_name"]
        i=request.session["user_id"]
        print(i, u)
    except KeyError:
        messages.error(request,"You need to ")

    return render(request, "user templates/user_seller.html")


def save_product(request):
    try:
        u=request.session["user_name"]
        i=request.session["user_id"]
        print(i, u)
    except KeyError:
        messages.error(request,"You need to ")

    pname = request.POST["p1"]
    bprice = request.POST["p2"]
    pinfo = request.POST["p3"]
    pimage = request.FILES["file"]
    print(pimage)
    pstatus = "bidding"
    print(pstatus)
    user_id = request.session['user_id']
    print(user_id)
    ProductModel(pname=pname, bprice=bprice, pinfo=pinfo, pimage=pimage, pstatus=pstatus, uinfo_id=user_id).save()
    messages.success(request,"your product is saved check in view_product below")
    return redirect("user_seller")


def view_product(request):
    try:
        u=request.session["user_name"]
        i=request.session["user_id"]
        print(i, u)
    except KeyError:
        messages.error(request,"You need to ")
    us=ProductModel.objects.filter(uinfo_id=request.session['user_id'])
    paginator = Paginator(us, 4)  # Show 25 contacts per page

    page = request.GET.get('page')
    us = paginator.get_page(page)
    return render(request,"user templates/view_product.html",{"use_product":us})


def Bid_product(request):
    try:
        u=request.session["user_name"]
        i=request.session["user_id"]
        print(i, u)
    except KeyError:
        messages.error(request,"You need to ")
    qs=ProductModel.objects.filter(pstatus="bidding") & ProductModel.objects.filter(~Q(uinfo_id=request.session['user_id']))

    paginator = Paginator(qs, 4)  # Show 25 contacts per page

    page = request.GET.get('page')
    qs = paginator.get_page(page)
    return render(request,"user templates/Bid_product.html",{"remain_user":qs})

def bid_details(request):
    try:
        u=request.session["user_name"]
        i=request.session["user_id"]
        print(i, u)
    except KeyError:
        messages.error(request,"You need to ")
    bamount=request.POST["b1"]
    pid=request.POST["b2"]
    uid = request.POST["b3"]
    BidTable(bid_price=bamount,pid_id=pid,uid_id=uid).save()
    return redirect("Bid_product")


def bid_show(request):
    try:
        u=request.session["user_name"]
        i=request.session["user_id"]
        print(i, u)
    except KeyError:
        messages.error(request,"You need to ")
    pid = request.GET.get("pid")
    print(pid)
    qs=BidTable.objects.filter(pid_id=pid)
    d = {"pid": pid}
    print(d)

    return render(request,"user templates/bid_show.html",{"data":qs,"pno":d})


def viewbid_show(request):
    try:
        u=request.session["user_name"]
        i=request.session["user_id"]
        print(i, u)
    except KeyError:
        messages.error(request,"You need to ")
    pid=request.GET.get("pid")
    qs=BidTable.objects.filter(pid_id=pid)
    d={"pid":pid}
    return render(request,"user templates/viewbid_show.html",{"data":qs,"pno":d})