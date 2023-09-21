from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
#class Redirect(RedirectView):
    #permanent = False
    #url = 'http://127.0.0.1:8000/news/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('protect.urls')),
    path('news/', include('NewsPaper.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
    path('appointments/', include(('appointments.urls', 'appointments'), namespace='appointments')),
]
