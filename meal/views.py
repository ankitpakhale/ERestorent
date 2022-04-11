from django.shortcuts import render,redirect
from .models import TableDetail,TableBooking,Administrative,Finalbooked
from app1.models import Site_User
from django.contrib import messages

def tablebooking(request,table_no):
    if 'user' in request.session:
        user = Site_User.objects.get(email=request.session['user'])
        table=TableDetail.objects.get(Table_No=table_no)
        print(table)
        try:
            if request.method=="POST":
                model=TableBooking()
                model.usereamil=user
                model.table_no=table
                model.time1=request.POST['time1']
                model.date=request.POST['date']
                model.booked=True

                model.save()
                messages.info(request, f"Table is Booked already..")  
        except:
            messages.error(request, f"Table is Booked already..")  
    else:
        return redirect('login')
    return render(request,'booking.html',{'user':user,'table':table})


def show_all(request):
    if 'email' in request.session:
        data=TableDetail.objects.all()
        return render(request,'alltable.html',{'data':data})
    else:
        data=TableDetail.objects.all()
        return render(request,'alltable.html',{'data':data})





def alltablebook(request):
    if 'email' in  request.session:   
        all=TableBooking.objects.all()
        return render(request,'allshow.html',{'all':all})
    else:
        return redirect('login_admin')

def Account_status(request):
    if 'email' in  request.session:
        z = TableBooking.objects.all().filter(booked=False)
        print(z)
        return render(request, 'account_status.html', {'z': z})
    else:
        return redirect('login_admin')
        
def edit(request,id):
    if 'email' in  request.session:
        table=TableBooking.objects.get(id=id)

        return render(request,'edit.html',{'table':table})
    else:
        return redirect('login_admin')

def Approve_acc(request, id):
    if 'email' in  request.session:
        user=Site_User.objects.get(email=request.session['user'])
        print(user)
        z1 =TableBooking.objects.get(id=id)
        z1.booked=request.POST['booked']
        z1.save()
        z.table_no.is_available=False
        z.save()
        print(z)
        print('data saved')
        return redirect('/allshow/')
    return render(request, 'Approve.html', {'z': z})
    else:
        return redirect('/login_admin/')


def login_admin(request):
    if request.method == 'POST':
        print("done")
        try:
            email = request.POST['ema']
            password = request.POST['pas']
            user = Administrative.objects.get(email=email)
            print(user)
            if user.password == password:
                request.session['email'] = email
                print("loged")
                request.session['email'] = email
                return redirect('/allshow/')
            else:
                messages.error(request, "Wrong Password")
                return redirect('/login_admin/')
        except:
            messages.error(request, "Wrong Email Address")
            return redirect('/login_admin/')
    return render(request, 'login_admin.html')

def signup_admin(request):
    if request.POST:
        obj = Administrative()
        obj.name = request.POST['name']
        obj.dob = request.POST['dob']
        obj.email = request.POST['email']
        obj.m_no = request.POST['mobile_no']
        obj.password = request.POST['password']
        obj.save()
        return redirect('login_admin')
    return render(request,'signup_admin.html')

def logout_admin(request):
    if request.session.has_key('email'):
        del request.session['email']
        return redirect('/login_admin/')
    else:
        return redirect('/login_admin/')

def mainslip(request,id):
    if 'user' in request.session:
        data=get_object_or_404(Finalbooked,id=id)
        print(data)
    else:
        return redirect('login')
    return render(request,'mainslip.html',{'data':data})