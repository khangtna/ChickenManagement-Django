from django.urls import path, include

from rest_framework import routers

from . import views


router= routers.DefaultRouter()
# router.register('all', views.apigetAllEMP, 'allemp')
router.register('abc', views.apiEMP)
router.register('all', views.apigetEMP, 'idemp')

# app_name= 'emp'

urlpatterns = [

    path('emp/', include(router.urls)),

    path('', views.api_getAllEmp, name='emp'),
    path('create', views.api_createEmp, name='create'),
    
    path('<id>/', views.api_getIDEmp, name='empID'),   
    path('<id>/update', views.api_updateEmp, name='update'),
    path('<id>/delete', views.api_delEmp, name='delete'),
    

]
