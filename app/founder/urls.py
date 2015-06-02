from django.conf.urls import patterns, url,include
from app.founder import views

urlpatterns = patterns('',
    #List of founders
    url(r'^$', views.FounderIndex.as_view(), name='index'),
    #Detail of a founder
    url(r'^(?P<pk>\d+)$', views.FounderView.as_view(), name='detail'),
    #Form for update the profile
    url(r'^profile/(?P<pk>\d+)$', views.FounderUpdate.as_view(), name='update'),
)