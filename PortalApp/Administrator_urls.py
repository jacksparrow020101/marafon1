from django.urls import path

from PortalApp.Administrator_views import Bash_Sahypa, Administrtor_Esasy_Surat, Administrator_Esasy_Surat_Create, \
    Administrator_Esasy_Sahypa_Update, Administrator_Esasy_Sahypa_Delete, Administrator_Syyasy_Habar_List, \
    Administrator_Syyasy_Habar_Create, Administrator_Syyasy_Habar_Update, Administrator_Syyasy_Habar_Delete, \
    Administrator_Tehnologiya_Habar_List, Administrator_Tehnologiya_Habar_Create, \
    Administrator_Tehnologiya_Habar_Update, Administrator_Tehnologiya_Habar_Delete, Administrator_Sport_Habar_List, \
    Administrator_Sport_Habar_Create, Administrator_Sport_Habar_Update, Administrator_Sport_Habar_Delete, \
    Administrator_Harby_Habar_List, Administrator_Harby_Habar_Create, Administrator_Harby_Habar_Update, \
    Administrator_Harby_Habar_Delete, Administrator_Gazet_List, Administrator_Gazet_Create, Administrator_Gazet_Update, \
    Administrator_Gazet_Delete, Administrator_Zurnal_List, Administrator_Zurnal_Create, Administrator_Zurnal_Update, \
    Administrator_Zurnal_Delete, Administrator_Surat_List, Administrator_Surat_Create, Administrator_Surat_Update, \
    Administrator_Surat_Delete, Administrator_Wideo_List, Administrator_Wideo_Create, Administrator_Wideo_Update, \
    Administrator_Wideo_Delete

urlpatterns = [
    path('', Bash_Sahypa.as_view(), name='Administrator_Bash_Sahypa'),
    path('Esasy_Surat/', Administrtor_Esasy_Surat.as_view(), name='Administrator_Esasy_Surat'),
    path('Esasy_Surat_Create/', Administrator_Esasy_Surat_Create.as_view(), name='Administrator_Esasy_Surat_Create'),
    path('Esasy_Sahypa_Update/<pk>/', Administrator_Esasy_Sahypa_Update.as_view(), name='Administrator_Esasy_Sahypa_Update'),
    path('Esasy_Sahypa_Delete/<pk>/',Administrator_Esasy_Sahypa_Delete.as_view(),name='Administrator_Esasy_Sahypa_Delete'),
    path('Syyasy_Habarlar/',Administrator_Syyasy_Habar_List.as_view(),name='Administrator_Syyasy_Habar_List'),
    path('Syyasy_Habar_Create/',Administrator_Syyasy_Habar_Create.as_view(),name='Administrator_Syyasy_Habar_Create'),
    path('Syyasy_Habar_Update/<pk>/',Administrator_Syyasy_Habar_Update.as_view(),name='Administrator_Syyasy_Habar_Update'),
    path('Syyasy_Habar_Delete/<pk>/',Administrator_Syyasy_Habar_Delete.as_view(),name='Administrator_Syyasy_Habar_Delete'),
    path('Tehnologiya_Habar_List/',Administrator_Tehnologiya_Habar_List.as_view(),name='Administrator_Tehnologiya_Habar_List'),
    path('Tehnologiya_Habar_Create/',Administrator_Tehnologiya_Habar_Create.as_view(),name='Administrator_Tehnologiya_Habar_Create'),
    path('Tehnologiya_Habar_Update/<pk>/',Administrator_Tehnologiya_Habar_Update.as_view(),name='Administrator_Tehnologiya_Habar_Update'),
    path('Tehnologiya_Habar_Delete/<pk>/',Administrator_Tehnologiya_Habar_Delete.as_view(),name='Administrator_Tehnologiya_Habar_Delete'),
    path('Sport_Habar_List/',Administrator_Sport_Habar_List.as_view(),name='Administrator_Sport_Habar_List'),
    path('Sport_Habar_Create/',Administrator_Sport_Habar_Create.as_view(),name='Administrator_Sport_Habar_Create'),
    path('Sport_Habar_Update/<pk>/',Administrator_Sport_Habar_Update.as_view(),name='Administrator_Sport_Habar_Update'),
    path('Sport_Habar_Delete/<pk>/',Administrator_Sport_Habar_Delete.as_view(),name='Administrator_Sport_Habar_Delete'),
    path('Harby_Habar_List/',Administrator_Harby_Habar_List.as_view(),name='Administrator_Harby_Habar_List'),
    path('Harby_Habar_Create/',Administrator_Harby_Habar_Create.as_view(),name='Administrator_Harby_Habar_Create'),
    path('Harby_Habar_Update/<pk>/',Administrator_Harby_Habar_Update.as_view(),name='Administrator_Harby_Habar_Update'),
    path('Harby_Habar_Delete/<pk>/',Administrator_Harby_Habar_Delete.as_view(),name='Administrator_Harby_Habar_Delete'),
    path('Gazet_List/',Administrator_Gazet_List.as_view(),name='Administrator_Gazet_List'),
    path('Gazet_Create/',Administrator_Gazet_Create.as_view(),name='Administrator_Gazet_Create'),
    path('Gazet_Update/<pk>/',Administrator_Gazet_Update.as_view(),name='Administrator_Gazet_Update'),
    path('Gazet_Delete/<pk>/',Administrator_Gazet_Delete.as_view(),name='Administrator_Gazet_Delete'),
    path('Zurnal_List/',Administrator_Zurnal_List.as_view(),name='Administrator_Zurnal_List'),
    path('Zurnal_Create/',Administrator_Zurnal_Create.as_view(),name='Administrator_Zurnal_Create'),
    path('Zurnal_Update/<pk>/',Administrator_Zurnal_Update.as_view(),name='Administrator_Zurnal_Update'),
    path('Zurnal_Delete/<pk>/',Administrator_Zurnal_Delete.as_view(),name='Administrator_Zurnal_Delete'),
    path('Surat_List',Administrator_Surat_List.as_view(),name='Administrator_Surat_List'),
    path('Surat_Create/',Administrator_Surat_Create.as_view(),name='Administrator_Surat_Create'),
    path('Surat_Update/<pk>/',Administrator_Surat_Update.as_view(),name='Administrator_Surat_Update'),
    path('Surat_Delete/<pk>/',Administrator_Surat_Delete.as_view(),name='Administrator_Surat_Delete'),
    path('Wideo_List',Administrator_Wideo_List.as_view(),name='Administrator_Wideo_List'),
    path('Wideo_Create/',Administrator_Wideo_Create.as_view(),name='Administrator_Wideo_Create'),
    path('Wideo_Update/<pk>/',Administrator_Wideo_Update.as_view(),name='Administrator_Wideo_Update'),
    path('Wideo_Delete/<pk>/',Administrator_Wideo_Delete.as_view(),name='Administrator_Wideo_Delete'),
]
