from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path("content/", views.content, name='content')
]
# content path should be updated to 
# path('<int:article_id>/content/', views.content, name='content')

