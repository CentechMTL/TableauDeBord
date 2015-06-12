from django.conf.urls import patterns, url, include

urlpatterns = patterns('app.kanboard.views',
   url(r'^board/(?P<board_slug>[\w-]+)/$', 'board', name='kanboard'),
   url(r'^board/(?P<board_slug>[\w-]+)/update/$', 'update'),
)

