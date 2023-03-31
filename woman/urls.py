from .views import *
from django.urls import path, re_path

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('woman/<slug:cat>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]
