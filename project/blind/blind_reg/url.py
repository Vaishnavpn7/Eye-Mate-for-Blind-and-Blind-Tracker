from django.conf.urls import url
from blind_reg import views
urlpatterns=[
    url('blindreg/',views.blindreg),
    url('viewblind/',views.viewblind),
    url('search/',views.search),
    url('^req/(?P<idd>\w+)',views.set, name='req'),

]