from django.shortcuts import render
from login.models import Login

# Create your views here.

# def login(request):
#     if request.method=='POST':
#         obj=Login()
#         obj.username=request.POST.get('name')
#         obj.password=request.POST.get('pass')
#         obj.save()
#     return render(request,'login/login.html')
def login(request):
    if request.method == "POST":
        uname = request.POST.get("log")
        passw = request.POST.get("pass")
        obj = Login.objects.filter(username=uname, password=passw)
        tp = ""
        for ob in obj:
            tp = ob.type
            uid = ob.u_id
            if tp == "admin":
                request.session["uid"] = uid
                return render(request, 'temp/admin_home.html')
            elif tp == "caretaker":
                request.session["uid"] = uid
                return render(request, 'temp/caretaker.html')
            elif tp == "friend":
                request.session["uid"] = uid
                return render(request, 'temp/friend home.html')
            # else:
        objlist = "Username or Password incorrect... Please try again...!"
        context = {
            'msg': objlist,
        }
        return render(request, 'login/login.html', context)
    return render(request,'login/login.html')
