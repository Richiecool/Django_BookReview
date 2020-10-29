from django.conf.urls import url
from . import views         

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^successregistration/$', views.successregistration, name="successregistration"),

    url(r'^success/$', views.success, name="success"),

    url(r'^successlogin/$', views.successlogin, name="successlogin"),

    url(r'^login/$', views.login, name="login"),

    url(r'^loadaddreview/$', views.loadaddreview, name="loadaddreview"),

    # url(r'^addreview$', views.addreview, name="addreview"),

    url(r'^addreview/(?P<id>\d+)$', views.addreview, name="addreview"),

    url(r'^addbookreview/$', views.addbookreview, name="addbookreview"),

    url(r'^addbookreview/(?P<id>\d+)/$', views.addbookreview, name="addbookreview"),

    url(r'^bookreview/(?P<id>\d+)/$', views.bookreview, name="bookreview"),

    url(r'^userreview/(?P<id>\d+)/$', views.userreview, name="userreview"),

    url(r'^delete_review/(?P<id>\d+)$', views.delete_review, name="delete_review"),

    url(r'^logout/$', views.logout, name="logout"),
]