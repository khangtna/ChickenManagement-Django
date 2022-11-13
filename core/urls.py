from django.urls import path

from .views import HomeView, base

from account.views import login



urlpatterns = [
    path('', login, name='login'),

    path('base/', base, name='base'),
]