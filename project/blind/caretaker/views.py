from django.shortcuts import render
from caretaker.models import Caretaker
from django.core.files.storage import FileSystemStorage
from login.models import Login
# Create your views here.
def carereg(request):
    if request.method=='POST':
        obj=Caretaker()
        obj.name=request.POST.get('caretakername')
        obj.password=request.POST.get('pass')
        obj.contact=request.POST.get('number')
        obj.email=request.POST.get('email')
        obj.place=request.POST.get('place')
        obj.district=request.POST.get('district')
        obj.pin=request.POST.get('pin')
        # obj.image=request.POST.get('pic')
        myfile = request.FILES['ppp']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.image = myfile.name
        obj.save()


    return render(request,'caretaker/caretaker reg.html')
def viewcare(request):
    obb=Caretaker.objects.all()
    context={

        'fulldetails':obb
    }
    return render(request,'caretaker/View caretaker admin.html',context)

def approve(request,idd):
    obb=Caretaker.objects.get(caretak_id=idd)
    obb.status="approved"
    obb.save()
    ob=Login()
    ob.username=obb.name
    ob.password=obb.password
    ob.type="caretaker"
    ob.u_id=obb.caretak_id
    ob.save()
    return viewcare(request)

def reject(request,idd):
    obb=Caretaker.objects.get(caretak_id=idd)
    obb.status="rejected"
    obb.save()
    return viewcare(request)

