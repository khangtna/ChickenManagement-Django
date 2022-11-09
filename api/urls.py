from django.urls import path, include

from rest_framework import routers

from . import views


router= routers.DefaultRouter()
router.register('emp', views.apiEMP)
router.register('category', views.apiCategory)
router.register('product', views.apiProduct)
router.register('account', views.apiAccount)

# app_name= 'emp'

urlpatterns = [

    path('', include(router.urls)),

    path('a/', views.api_getAllEmp, name='apiemp'),
    # path('create', views.api_createEmp, name='create'),
    
    path('<id>/', views.api_getIDEmp, name='empID'),   
    path('update/<id>/', views.api_updateEmp, name='update-emp'),
    # path('delete/<id>/', views.api_delEmp, name='delete'),
    

]
