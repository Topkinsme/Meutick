from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customer,AdminUser,Ticket,Categories
import random

def dashboard(request):
    if 'email' in request.session:
        return render(request,"mainpage/dashboard.html")
    return redirect('signin')



def catpage(request,mname):
    #eg1 - 10
    #gg1 - 15
    #lag1 - 20 
    #mag1 - 25
    #vf1 - 30
    names=["eg1","gg1","lag1","mag1","vf1"]
    display_names={"eg1":"Egyptian Gallery","gg1":"Gandhara Gallery","lag1":"Long Archaeology Gallery","mag1":"This Minor Art Gallery","vf1":"Varanda 1st Floor"}
    if 'email' in request.session:
        if request.method=="POST":
            try:
                price=int(request.POST['price'][:-2])
                tickets=int(request.POST['ticketcount'])
            except Exception as e:
                print(e)
                return redirect('dashboard')
            museum=Categories.objects.filter(name=mname)
            museum[0].tickets-=tickets
            museum[0].save()
            new_ticket=Ticket.objects.create(
                            tic_id=str(random.randint(10000,99999)),
                            cusname=Customer.objects.filter(email=request.session['email'])[0],
                            catname=Categories.objects.filter(name=mname)[0],
                            count=tickets,
                        )
            return redirect('profile')
        else:
            
            museum=Categories.objects.filter(name=mname)
            if len(museum)<1:
                    return redirect('dashboard')
            else:
                context={'m_name':display_names[museum[0].name],'price':museum[0].price}
                return render(request,"mainpage/catpage.html",context=context)
    return redirect('signin')


def editprofile(request):
    if 'email' in request.session:
        return render(request,"mainpage/edit-profile.html")
    return redirect('signin')

def profile(request):
    if 'email' in request.session:
        context={}
        cus=Customer.objects.filter(email=request.session['email'])[0]
        trxns=Ticket.objects.filter(cusname=cus)
        context['name']=cus.name
        context['email']=cus.email
        context['phno']=cus.phno
        context['trxns']=trxns
        return render(request,"mainpage/profile.html",context=context)
    return redirect('signin')

def signin(request):
    context={"error":""}
    if request.method=="POST":
        error=""
        email=request.POST['email']
        password=request.POST['password']
        user = Customer.objects.filter(email=email)
        if len(user)<1:
            error="User doesn't exist"
        elif user[0].password!=password:
            error="Incorrect password!"
        context['error']=error
        if error:
            return render(request,"mainpage/Sign_In.html",context)
        else:
            request.session['email']=user[0].email
            request.session.modified=True
            request.session.set_expiry(600)
            return redirect("dashboard")
    return render(request,"mainpage/Sign_In.html")

def signup(request):
    context={"error":""}
    if request.method=="POST":
        error=""
        name=request.POST['name']
        email=request.POST['email']
        phno=request.POST['mobile']
        password=request.POST['password']
        confpassword=request.POST['confirm-password']
        if len(phno)<10 or not phno.isdigit():
            error+="Phone number must be atleast 10 digits, and must only contain numbers. "
        if len(password)<7:
            error+="Password must atleast be 7 characters in length. "
        if password!=confpassword:
            error+="Passwords don't match."
        users = Customer.objects.filter(email=email)
        if len(users)>0:
            error+="This email already exists. Sign-in instead. "
        context['error']=error
        if error:
            return render(request,"mainpage/Sign_Up.html",context)
        else:
            new_customer=Customer.objects.create(
                        cus_id=str(random.randint(10000,99999)),
                        name=name,
                        email=email,
                        phno=phno,
                        password=password
                    )
            return redirect("/signin")
            
    return render(request,"mainpage/Sign_Up.html")


def adminpage(request):
    if 'email' in request.session:
        return render(request,"mainpage/adminpage.html")
    return redirect('signin')

def dev(request):
    if 'email' in request.session:
        return render(request,"mainpage/dev.html")
    return redirect('signin')


def landingpage(request):
    request.session.clear()
    request.session.flush()
    return render(request,"mainpage/landing_page.html")