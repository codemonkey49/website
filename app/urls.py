from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', index, name="index"),
    #url(r"profile",profile,name="profile"),
]