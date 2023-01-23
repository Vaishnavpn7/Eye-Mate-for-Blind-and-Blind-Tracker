from django.shortcuts import render
from friend.models import Friend
from django.core.files.storage import FileSystemStorage
from blind_reg.models import Requset
from login.models import Login

# Create your views here.

def friendreg(request):
    if request.method=='POST':
        obj=Friend()
        obj.name=request.POST.get('friend')
        obj.password=request.POST.get('pass')
        obj.contact=request.POST.get('number')
        obj.email=request.POST.get('email')
        obj.place=request.POST.get('place')
        obj.district=request.POST.get('district')
        obj.pin=request.POST.get('pin')
        # obj.image=request.POST.get('photo')
        myfile = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.image = myfile.name
        obj.blind_id=1
        obj.save()

        ob=Login()
        ob.username=obj.name
        ob.password=obj.password
        ob.type="friend"
        ob.u_id=obj.image
        ob.save()
    return render(request,'friend/friend reg.html')

def viewfriend(request):
    obb=Friend.objects.all()
    context={

        'details':obb
    }

    return render(request,'friend/view friend.html',context)
def approve(request,idd):
    obb=Requset.objects.get(f_id=idd)
    obb.status="approved"
    obb.save()
    return viewrequest(request)
# def reject(request,idd):
#     obb=Friend.objects.get(friend_id=idd)
#     obb.status="reject"
#     obb.save()
#     return viewrequest(request)
def viewrequest (request):
    vv= request.session["uid"]
    obb=Requset.objects.all()
    context={
        'requests':obb
    }
    return render(request,'friend/friend requests.html',context)

def rej(req,idd):
    object=Requset.objects.get(f_id=idd)
    object.delete()
    return viewrequest(req)



