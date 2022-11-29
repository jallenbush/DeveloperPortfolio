from django.urls import path
from . import views  

urlpatterns = [
#create path (in root) to all pages 
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('resume', views.resume, name='resume'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('contact', views.contact, name='contact'),
]
