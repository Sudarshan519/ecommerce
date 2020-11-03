
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
urlpatterns = [
    path('', views.index,name='home'),
    path('about/', views.about),
    path('contact/', views.contact),
    path('products/<int:myid>', views.productview, name='productview'),
    path('checkout/', views.checkout, name='checkout'),
    path('tracker/', views.tracker, name='tracker'),
    path('search/', views.search, name='search'),

]
