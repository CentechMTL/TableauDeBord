from django.conf.urls import patterns, url, include
from app.kanboard.views import BoardIndex

urlpatterns = patterns('app.kanboard.views',
   #url(r'^board/(?P<board_slug>[\w-]+)/$', 'board', name='kanboard'),
   url(r'^(?P<pk>\d+)/$', BoardIndex.as_view(), name='kanboard'),
   url(r'^(\d+)/update/$', 'update'),
)

