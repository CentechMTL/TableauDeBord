# coding: utf-8

from django.conf.urls import patterns, url, include
from app.finance import views

urlpatterns = patterns(
    '',
    url(
        r'^(\d+)/$',
        views.detailFinance.as_view(),
        name='detail_finance'
    ),

    # STOCK EXCHANGES
    url(
        r'bourse/add/(\d+)/$',
        views.BourseCreate.as_view(),
        name='bourse_add'
    ),
    url(
        r'bourse/update/(?P<pk>\d+)/$',
        views.BourseUpdate.as_view(),
        name='bourse_update'
    ),
    url(
        r'bourse/delete/(?P<pk>\d+)/$',
        views.BourseDelete.as_view(),
        name='bourse_delete'
    ),

    # SUBSIDIES
    url(
        r'subvention/add/(\d+)/$',
        views.SubventionCreate.as_view(),
        name='subvention_add'
    ),
    url(
        r'subvention/update/(?P<pk>\d+)/$',
        views.SubventionUpdate.as_view(),
        name='subvention_update'
    ),
    url(
        r'subvention/delete/(?P<pk>\d+)/$',
        views.SubventionDelete.as_view(),
        name='subvention_delete'
    ),

    # INVESTMENTS
    url(
        r'investissement/add/(\d+)/$',
        views.InvestissementCreate.as_view(),
        name='investissement_add'
    ),
    url(
        r'investissement/update/(?P<pk>\d+)/$',
        views.InvestissementUpdate.as_view(),
        name='investissement_update'
    ),
    url(
        r'investissement/delete/(?P<pk>\d+)/$',
        views.InvestissementDelete.as_view(),
        name='investissement_delete'
    ),

    # LOANS
    url(
        r'pret/add/(\d+)/$',
        views.PretCreate.as_view(),
        name='pret_add'
    ),
    url(
        r'pret/update/(?P<pk>\d+)/$',
        views.PretUpdate.as_view(),
        name='pret_update'
    ),
    url(
        r'pret/delete/(?P<pk>\d+)/$',
        views.PretDelete.as_view(),
        name='pret_delete'
    ),

    # SALES
    url(
        r'vente/add/(\d+)/$',
        views.VenteCreate.as_view(),
        name='vente_add'
    ),
    url(
        r'vente/update/(?P<pk>\d+)/$',
        views.VenteUpdate.as_view(),
        name='vente_update'
    ),
    url(
        r'vente/delete/(?P<pk>\d+)/$',
        views.VenteDelete.as_view(),
        name='vente_delete'
    ),
)
