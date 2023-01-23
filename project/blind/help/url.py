from django.conf.urls import url
from help import views
urlpatterns=[
    url('^viewhelp/',views.viewhelp),
    url('^viewhelpfriend/',views.viewhelpfriend),


]