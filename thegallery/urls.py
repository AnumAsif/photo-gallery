from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url(r'^gallery/(\d+)',views.gallery, name= 'categorypics'),
    url(r'^gallery/location/(\d+)', views.gallery_by_location, name="locationpics"),   
    url(r'^search/', views.search_results, name='search_results')    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)