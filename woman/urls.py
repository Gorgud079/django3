from .views import *
from django.urls import path, re_path

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login', login, name='login'),
    path('category/<int:cat_id>/', show_category, name='category'),
    path('post/<int:post_id>/', show_page, name='post'),
    path('woman/<slug:cat>/', categories),
    path('archive/<int:year>/', archive),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]
