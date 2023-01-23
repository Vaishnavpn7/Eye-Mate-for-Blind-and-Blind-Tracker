from django.conf.urls import url
from caretaker import views
urlpatterns=[
    url('^carereg/',views.carereg),
    url('^viewcare/',views.viewcare),
    url('^approve/(?P<idd>\w+)',views.approve, name='approve'),
    url('^reject/(?P<idd>\w+)',views.reject, name='rejected'),




]