from django.conf.urls import url
from temp import views
urlpatterns={

    url('^adminhome/',views.adminhome),
    url('^caretakerhome/',views.caretakerhome),
    url('^index/',views.index),
    url('^friendhome/',views.friendhome),
}