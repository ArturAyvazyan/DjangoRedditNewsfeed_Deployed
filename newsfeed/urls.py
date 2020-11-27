from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from redditfeed import views
from redditfeed.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^search/', views.search, name='search'),
    url(r'^zaplatka/', views.zaplatka, name='zaplatka'),
]
