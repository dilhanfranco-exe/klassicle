from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name="home"),
]

urlpatterns += staticfiles_urlpatterns()