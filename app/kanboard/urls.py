from django.conf.urls import patterns, url, include
from app.kanboard import views

urlpatterns = patterns(
    'app.kanboard.views',

    # kanboard of a company
    url(
        r'^(?P<pk>\d+)/$',
        views.BoardIndex.as_view(),
        name='kanboard'
    ),

    # Detail of a card
    url(
        r'^card/(?P<pk>\d+)/$',
        views.CardView.as_view(),
        name='card'
    ),

    # Ajax
    url(
        r'^(\d+)/update/$',
        views.update
    ),
    url(
        r'^(\d+)/add/$',
        views.addCard,
        name='kanboardAddCard'
    ),
    url(
        r'^addComment/(\d+)$',
        views.addComment,
        name='addComment'
    ),
    url(
        r'^delete/card/(\d+)$',
        views.deleteCard,
        name='kanboardDeleteCard'
    ),
    url(
        r'^getDetail/card/(\d+)$',
        views.getDetailCard,
        name='kanboardGetDetailCard'
    ),
    url(
        r'^getKanboard/(\d+)/([a-zA-Z]+)$',
        views.getDetailKanboard,
        name='getDetailKanboard'
    ),
)
