from django.shortcuts import render
from .models import InboxModel,OrganizationModel
from .forms import OrganizationForm
def indexPage(request):
    return render(request,"index.html")
def loginPage(request):
    return render(request, "login.html")
def checkUser(request):
    user = request.POST.get("username")
    password = request.POST.get("password")
    if user == "admin" and password == "admin":
        return render(request,"welcome.html")
    else:
        return render(request, "index.html", {"msg": "Invalid Details"})
def inboxPage(request):
    inbox_data = InboxModel.objects.all()
    return render(request, "inboxpage.html",{"data":inbox_data})
def organizationPage(request):
    org_form = OrganizationForm()
    return render(request,"organizationReg.html",{"data":org_form})
def saveOrganization(request):
    id = request.POST.get("org_id")
    name = request.POST.get("org_name")
    address = request.POST.get("org_address")
    country = request.POST.get("org_country")
    state = request.POST.get("org_state")
    city = request.POST.get("org_city")
    email =  request.POST.get("org_email")
    password = request.POST.get("org_password")
    contact = request.POST.get("org_contact")
    OrganizationModel(org_id=id, org_name=name, org_address=address,
                      org_country=country, org_state=state, org_city=city, org_email=email,
                      org_password=password, org_contact=contact).save()
    return render(request,"organizationReg.html",{"msg":"Organization Added Successfully"})

def viewOrg(request):
    org_data = OrganizationModel.objects.all()
    return render(request,"vieworg.html",{"org":org_data})

def deleteEmployee(request):
    id = request.GET.get("x")
    OrganizationModel.objects.filter(org_id=id).delete()
    org_data = OrganizationModel.objects.all()
    return render(request, "vieworg.html",{"org":org_data,"msg":"Organization Deleted Successfully"})

def logOut(request):
    return render(request, "login.html", {"message": "Logout Succesfully"})

def donorPage(request):
    return render(request,"donorpage.html")

def checkDonor(request):
   # donorname = request.
    return None
def donorReg(request):
    return render(request,"donorregistration.html")
def saveDonor(request):
    name = request.POST.get("d2")
    userid = request.POST.get("d3")
    password = request.POST.get("d4")
    gender = request.POST.get("d5")
    email = request.POST.get("d6")
    contact = request.POST.get("d7")
    bloddgroup = request.POST.get("d8")
    state = request.POST.get("d9")
    city = request.POST.get("d10")
    age = request.POST.get("d11")
    weight = request.POST.get("d12")
    donate_date = request.POST.get("d13")
    OrganizationModel(org_id=id, org_name=name, org_address=address,
                      org_country=country, org_state=state, org_city=city, org_email=email,
                      org_password=password, org_contact=contact).save()
    return render(request, "organizationReg.html", {"msg": "Organization Added Successfully"})

