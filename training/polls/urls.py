from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('index2', views.index2, name='index2'),
    path('index3', views.index3, name='index3'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    path('detail2/<int:question_id>/', views.detail2, name='detail2'),
    path('detail3/<int:question_id>/', views.detail3, name='detail3'),
    
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]