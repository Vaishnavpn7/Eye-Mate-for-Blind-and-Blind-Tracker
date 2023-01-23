from django.conf.urls import url
from complaint import views
urlpatterns=[
    url('^cmplt/',views.cmplt),
    # url('app/(?P<idd>\w+)',views.posrep,name='app'),
    url('app/(?P<idd>\w+)',views.posrep,name='app'),
    url('^viewcom/',views.viewcom),
    url('viewreply/',views.viewreply),





]