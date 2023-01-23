from django.shortcuts import render
from location.models import Location
# Create your views here.
def blindloc(request):
    obb=Location.objects.all()
    context={

        'location':obb
    }


    return render(request,'location/blind location.html',context)
def locationfriend(request):
    obb=Location.objects.all()
    context={

        'locationfriend':obb

    }
    return render(request,'location/location friend.html',context)

