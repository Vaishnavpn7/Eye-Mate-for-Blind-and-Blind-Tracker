from django.shortcuts import render
from complaint.models import Complaint
import datetime


# Create your views here.
def cmplt(request):
    if request.method == 'POST':
        obj = Complaint()
        obj.complaint = request.POST.get('comp')
        obj.caretak_id = 1
        obj.date = datetime.date.today()
        obj.time = datetime.datetime.now()
        obj.reply='pending'
        obj.save()
    return render(request, 'complaint/post complaint.html')


def posrep(request,idd):
    if request.method == 'POST':
        obj = Complaint.objects.get(comp_id=idd)
        obj.reply = request.POST.get('reply')
        obj.caretak_id = 1
        obj.date = datetime.date.today()
        obj.time = datetime.datetime.now()
        obj.save()
        return viewcom(request)
    return render(request, 'complaint/post reply.html')


def viewcom(request):
    obb = Complaint.objects.all()

    context = {

        'complaint': obb
    }
    return render(request,'complaint/view complaint.html', context)
def viewreply(request):
    obb = Complaint.objects.all()

    context = {

        'reply' : obb
    }
    return render(request,'complaint/viewreply.html',context)
