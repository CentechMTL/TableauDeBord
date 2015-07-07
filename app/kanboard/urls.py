from django.conf.urls import patterns, url, include
from app.kanboard.views import BoardIndex, addCard, deleteCard, getDetailCard, getDetailKanboard

urlpatterns = patterns('app.kanboard.views',
   #url(r'^board/(?P<board_slug>[\w-]+)/$', 'board', name='kanboard'),
   url(r'^(?P<pk>\d+)/$', BoardIndex.as_view(), name='kanboard'),
   url(r'^(\d+)/update/$', 'update'),

   url(r'^(\d+)/add/$', addCard, name='kanboardAddCard'),
   url(r'^delete/card/(\d+)$', deleteCard, name='kanboardDeleteCard'),
   url(r'^getDetail/card/(\d+)$', getDetailCard, name='kanboardGetDetailCard'),
   url(r'^getKanboard/(\d+)$', getDetailKanboard, name='getDetailKanboard'),
)