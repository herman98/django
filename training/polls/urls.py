from django.urls import path

from . import views

urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
]