from django.urls import path
from . import views

app_name = 'resume'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
]
