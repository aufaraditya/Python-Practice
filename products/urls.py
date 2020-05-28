from django.urls import path
from . import views #. (dot) to make sure the views imported is the one from the current folder


urlpatterns = [
    path('', views.index),
    path('new/', views.new)
]