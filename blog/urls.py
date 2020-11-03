
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
urlpatterns = [
    path('postComment',views.postComment,name='postComment'),
    
    
    
    path('', views.index),
    path('<str:slug>/', views.blogpost,name='blogHome'),
]
