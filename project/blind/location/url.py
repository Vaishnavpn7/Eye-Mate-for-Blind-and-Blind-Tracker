from django.conf.urls import url
from location import views
urlpatterns=[
    url('^blindloc',views.blindloc),
    url('locationfriend',views.locationfriend),



]