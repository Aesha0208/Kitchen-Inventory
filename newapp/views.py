from django.shortcuts import render,redirect
from newapp.form import *
from newapp.models import *

def home(request):
    label = []
    data = []
    queryset=Add_Inventory.objects.order_by('-Quantity')[:5]
    for a in queryset:
        label.append(a.Product)
        data.append(a.Quantity)

    label2 = []
    data2 = []
    queryset2=Add_Inventory.objects.order_by('Quantity')[:5]
    for b in queryset2:
        label2.append(b.Product)
        data2.append(b.Quantity)

    label3 = []
    data3 = []
    queryset3=Add_Inventory.objects.all()
    for c in queryset3:
        label3.append(c.Product)
        data3.append(c.Quantity)

    return render(request, 'home.html',
    {
        'label':label,
        'data':data,
        'label2':label2,
        'data2':data2,
        'label3':label3,
        'data3':data3,
    })

    # return render(request, 'home.html')


def contact(request):
     return render(request,"contactUs.html",context={"msg":"Contact Us Page"})

def about(request):
      return render(request,"aboutUs.html",context={"msg":"About Us Page"})
    
def kitchenInv(request):
    return render(request,"kitchenList.html",context={"msg":"Inventory"})


def AddInv(request):
    form = AddInvForm(request.POST or None)
    context = {'forms':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            objDetails = Add_Inventory.objects.all()
            return render(request,"addInv.html", context={"forms":form,"data":objDetails})
        else:
            return render(request,"addInv.html", context={"forms":form,"msg":"Error"})
    return render(request, "addInv.html", context={"forms":AddInvForm()})


def CreateInv(request):
    form = CreateInvForm(request.POST or None)
    context = {'forms':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            Details = Create_Inventory.objects.all()
            return render(request,"create.html", context={"forms":form,"data":Details})
        else:
            return render(request,"create.html", context={"forms":form,"msg":"Error"})
    return render(request, "create.html", context={"forms":CreateInvForm()})

def UpdateInv(request,id):
    product_details = Add_Inventory.objects.all()
    specific_product_= Add_Inventory.objects.filter(id=id).last()
    print("User Product ---->(user_product_)")
    if request.method == "POST":
        product = request.POST.get("Product")
        qty = request.POST.get("Quantity")

        updObj = Add_Inventory.objects.filter(id=id).update(Product=product,Quantity=qty)

        if updObj:
            return redirect("updateInvList")
        else:
            return render(request,'updateInv.html',context={'form':AddInvForm(),"error":"invalid user"})
    context={'form':AddInvForm(),"data":product_details, 'editValue':specific_product_,'edit':True,'id':id }
    return render(request, "updateInv.html", context=context )

def UpdateInvList(request):
    product_details = Add_Inventory.objects.all()
    print("User Product ---->(user_product_)")
    context={"data":product_details}
    return render(request, "updateInv.html", context=context )

def DelInv(request,id):
    printdata=Add_Inventory.objects.get(id=id)
    printdata.delete()
    data=Add_Inventory.objects.all()
    return render(request, 'updateInv.html', {'data':data})
