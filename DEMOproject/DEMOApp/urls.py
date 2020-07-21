from django.urls import path
from . import views


urlpatterns = [
    path('', views.dbuddy, name='dbuddy'),
    path('home', views.home, name='home'),
    path('about', views.about, name='custnumber'),
    path('contact', views.contact, name='contact-page'),
    path('memos', views.memos, name='memos'),
    path('surveys',views.surveys, name='surveys'),
    path('surveys1',views.surveys1, name='surveys1'),
    path('dbuddy',views.dbuddy, name='dbuddy'),
]