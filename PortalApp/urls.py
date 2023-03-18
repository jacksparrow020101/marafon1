from django.urls import path

from PortalApp.views import *

urlpatterns = [
    path('', Bash_Sahypa.as_view(), name='Bash_Sahypa'),
    path('Syyasy_Habar/<pk>/', Syyasy_Habar.as_view(), name='Syyasy_Habar'),
    path('Syyasy_Habarlar/', Syyasy_Habarlar.as_view(), name='Syyasy_Habarlar'),
    path('Tehnologiya_Habar/<pk>/', Tehnologiya_Habar.as_view(), name='Tehnologiya_Habar'),
    path('Tehnologiya_Habarlar/', Tehnologiya_Habarlar.as_view(), name='Tehnologiya_Habarlar'),
    path('Sport_Habar/<pk>/', Sport_Habar.as_view(), name='Sport_Habar'),
    path('Sport_Habarlar/', Sport_Habarlar.as_view(), name='Sport_Habarlar'),
    path('Harby_Habar/<pk>/', Harby_Habar.as_view(), name='Harby_Habar'),
    path('Harby_Habarlar/', Harby_Habarlar.as_view(), name='Harby_Habarlar'),
    path('Gazetler/', Gazetler.as_view(), name='Gazetler'),
    path('Metbugat_count/<path:url>/<pk>/<type>/',Metbugat_count,name='Metbugat_count'),
    path('Gazet/<name>/', Gazet.as_view(), name='Gazet'),
    path('Zurnallar/', Zurnallar.as_view(), name='Zurnallar'),
    path('Zurnal/<name>/',Zurnal.as_view(),name='Zurnal'),
    path('Wideo/',Wideo.as_view(),name='Wideo'),
    path('Surat/',Surat.as_view(),name='Surat'),
]
