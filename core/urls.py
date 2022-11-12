from django.urls import path

from .views import HomeView, Home

from account.views import login



urlpatterns = [
    path('', login, name='login'),

    path('user/', Home, name='user'),
]