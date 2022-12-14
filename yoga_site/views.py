import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Customer
from .models import Payment
from datetime import date
from datetime import timedelta
# Create your views here.

def test(request):
    context={'name': 'tarab'}
    return render(request, "index.html", context)

today = date.today()
index=0

def enrollment(request):
    context={"error": False}
    context={"errorAge": False}
    context={"saved": False}
    if request.method=="POST":
        data=request.POST
        Name=data["name"]
        Email=data["email"]
        Phnno=data["phnno"]
        Age=data["age"]
        Batch=data["batch"]
        Password=data["password"]

        AgeInt=int(Age)
        if AgeInt<18 or AgeInt>65 :
            context["errorAge"]=True
            print("Age Limitation")
            return render(request, "enroll.html", context)

        
        '''if(data["genderM"]=="on"):
            Gender="Male"
        elif (data["genderF"]=="on"):
            Gender="Female"
        elif (data["genderP"]=="on"):
            Gender="Secret"'''
        #list=[]
        eDate = today + timedelta(days=30)
        #list.append(Payment(today, Batch, 30))

        try:
            #dct={'st_Date':today, 'end_Date':eDate, 'bat_ch':Batch, 'balance':30}
            obj=Customer(CustName=Name, CustEmail=Email, CustPhnno=Phnno, CustAge=AgeInt, CustBatch=Batch, CustPswd=Password, PaymentDate=today)
            obj.save()  
            l1=Payment(st_date=today, end_date=eDate, ba_tch=Batch, balance=30, user_of_payment=obj)
            l1.save()  
            context["saved"]=True
            print("No error in saving new user")
           
        except:
            context["error"]=True
            print("Error coming")
            #return False
    else:
        print("User Request Not Suvmitted")

    return render(request, "enroll.html", context)

def findBatch(obj):
    row_payment=Payment.objects.filter(user_of_payment=obj)    #saare objects nikalo jinme name user ke name hai
    for x in row_payment:
        if x.st_date<=today and x.end_date>=today:
            return x.ba_tch

def findBal(obj):
    delta= obj.payment_set.last().end_date - today
    return int(delta.days)


def login(request):
    context={"wrongPswd":False}
    context={"usernotexist":False}

    if request.method=="POST":
        data=request.POST
        name=data["name"]
        pswd=data["password"]
        row=Customer.objects.filter(CustName=name)
        print(len(row))

        if (len(row)==0):
            #User exist hi nhi krrha, it means row is empty, koi object nhi aaya
            context["usernotexist"]=True
            print("User does not exist")
            return render(request, "login.html", context)

        obj=row[0]      #obj=row ke objects ka phla object 

        if(obj.CustPswd==pswd):
            #Password username ke sath match hai, i.e., ek hi object me aarhe hain
            context={
                'obj': obj
            }
            currBatch=findBatch(obj)
            currBalance=findBal(obj)
            allPayments=Payment.objects.filter(user_of_payment__CustName=obj.CustName)
            context={
                'currBatch': currBatch,
                'currBalance': currBalance,
                'CustName': obj.CustName,
                'CustEmail': obj.CustEmail,
                'CustPhnno': obj.CustPhnno,
                'CustPswd': obj.CustPswd,
                'CustAge': obj.CustAge,
                'PaymentDate': obj.PaymentDate,
                'allPayments': allPayments,
                'PaymentHistory': len(allPayments)
            }
            print("currbalance: "+ str(context["currBalance"]))
            print(obj.CustPhnno)
            return render(request, "profile.html", context)
        else:
            #Username ka object ka password given inout pswd se match ni hua
            print("Wrong X")
            context["wrongPswd"]=True
            return render(request, "login.html", context)

    else:
        print("User did not subitted any request")
    return render(request, "login.html", context)

def CompletePayment(request):
    context={'chalgya': False}
    if(request.GET.get('PayNext')):
        data=request.GET
        newbatch=data["newbatch"]
        CustName=data["objCustName"]
        
        context["chalgya"]=True
        row=Customer.objects.filter(CustName=CustName)
        obj=row[0] 
        currBatch=findBatch(obj)
        currBalance=findBal(obj)
        st_date=obj.payment_set.last().end_date + timedelta(days=1)
        end_date=st_date + timedelta(days=30)
        ba_tch=newbatch
        balance=currBalance+30
        l2=Payment(st_date=st_date, end_date=end_date, ba_tch=ba_tch, balance=balance, user_of_payment=obj)
        l2.save()
        currBalance=findBal(obj)
        allPayments=Payment.objects.filter(user_of_payment__CustName=obj.CustName)
        

        print("CompletePayment function "+CustName)
        context={
                'currBatch': currBatch,
                'currBalance': currBalance,
                'CustName': obj.CustName,
                'CustEmail': obj.CustEmail,
                'CustPhnno': obj.CustPhnno,
                'CustPswd': obj.CustPswd,
                'CustAge': obj.CustAge,
                'PaymentDate': obj.PaymentDate,
                'allPayments': allPayments,
                'PaymentHistory': len(allPayments)
            }

    return render(request, "profile.html", context)
