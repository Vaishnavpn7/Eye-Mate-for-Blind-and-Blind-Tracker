from django.conf.urls import url
from friend import views
urlpatterns=[

    url('^friendreg/',views.friendreg),
    url('viewfriend/',views.viewfriend),
    url('viewrequests/',views.viewrequest),
    url('^approve/(?P<idd>\w+)',views.approve,name='approved'),
    url('^rej/(?P<idd>\w+)',views.rej,name='rej'),
]