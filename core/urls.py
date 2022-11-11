from django.urls import path

from .views import HomeView

from account.views import login

urlpatterns = [
    path('', login, name='login'),
]