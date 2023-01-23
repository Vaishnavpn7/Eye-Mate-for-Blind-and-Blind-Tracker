from django.shortcuts import render
from blind_reg.models import BlindReg
from blind_reg.models import Requset
from django.core.files.storage import FileSystemStorage
from friend.models import Friend


# Create your views here.
def blindreg(request):
    if request.method == 'POST':
        obj = BlindReg()
        obj.name = request.POST.get('blindpersonname')
        obj.password = request.POST.get('pass')
        obj.place = request.POST.get('place')
        obj.email = request.POST.get('email')
        obj.contact = request.POST.get('number')
        obj.district = request.POST.get('district')
        obj.pin = request.POST.get('pin')
        # obj.image = request.POST.get('photo')
        myfile=request.FILES['photo']
        fs=FileSystemStorage()
        filename =fs.save(myfile.name, myfile)
        obj.image=myfile.name
        obj.save()
    return render(request, 'blind_reg/blind reg.html')


def viewblind(request):
    obb = BlindReg.objects.all()
    context = {
        'details': obb
    }

    return render(request, 'blind_reg/View blind person admin.html', context)

def search(request):
    np = request.POST.get('name')

    if request.method=="POST":

        obj=BlindReg.objects.filter(name__icontains=np)

        context={
            'objval':obj,

        }
        return render(request,'blind_reg/Search.html',context)
    return render(request,'blind_reg/Search.html')


def set(req,idd):
    vv = req.session["uid"]
    object=BlindReg.objects.get(blind_id=idd)
    # ob=Friend()
    obj=Requset()
    obj.name=vv
    obj.friend_id=vv
    obj.place=object.place
    obj.pin=object.pin
    obj.phone=object.contact
    obj.photo=object.image
    obj.save()
    return search(req)
# def search(request):
    # return render(request, 'blind_reg/Search.html')
