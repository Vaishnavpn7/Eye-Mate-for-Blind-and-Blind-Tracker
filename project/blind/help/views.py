from django.shortcuts import render
from help.models import Help

# Create your views here.
def viewhelp(request):
    obb=Help.objects.all()
    context={

        'helpdetails':obb
    }
    return render(request,'help/view help.html',context)
def viewhelpfriend(request):
    obb=Help.objects.all()
    context={

        'helpfrind':obb

    }
    return render(request,'help/view help friend.html',context)

