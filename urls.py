from . import views
from django.urls import path

app_name = 'personal_blogs'
urlpatterns = [
    path('', views.home, name='home'),
]

