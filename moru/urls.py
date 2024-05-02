from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking', views.booking, name='booking'),
    path('about/', views.about, name='about'),
    path('amzingwild/', views.amazing, name='amazingwild'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('blog/', views.blog, name='blog'),
    path('hotels/', views.hotels, name='hotels'),
    path('safaris/', views.safaris, name='safaris'),
    path('tours/', views.tours, name='tours'),
    path('ultimateeastafrica/', views.ultimateeastafrica, name='ultimateeastafrica'),
    path('visitkenya/', views.visitkenya, name='visitkenya'),
    path('visittz/', views.visittz, name='visittz'),
    path('visituganda', views.visituganda, name='visituganda'),
    path('visitrwanda', views.visitrwanda, name='visitrwanda')
]