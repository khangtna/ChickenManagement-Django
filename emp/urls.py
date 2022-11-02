from django.urls import path, include

from rest_framework import routers

from . import views
# from .views import GetAllEMPAPIView, GetAllEMPViewSet

# router= routers.DefaultRouter()
# router.register('api-1', views.GetAllEMPViewSet)

urlpatterns = [
    # path('api/', include(router.urls)),

    # path('api/', views.GetAllEMPAPIView.as_view(), name='empapi'),


    path('', views.getAllEMP, name='emp'),
    path('add/', views.addEMP, name='addemp'),

    
]
