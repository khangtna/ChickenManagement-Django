from django.urls import path, include

from rest_framework import routers

from knox import views as knox_views

from . import views


router= routers.DefaultRouter()
router.register('emp', views.apiEMP)
router.register('category', views.apiCategory)
router.register('product', views.apiProduct)
router.register('account', views.apiAccount)
router.register('permission', views.apiPermission)
router.register('user', views.apiUser)

# app_name= 'emp'

urlpatterns = [

    path('', include(router.urls)),

    #register
    path('register/', views.RegisterAPI.as_view(), name='api-register'),
    path('login/', views.LoginAPI.as_view(), name='api-login'),
    path('logout/', knox_views.LogoutView.as_view(), name='api-logout'),
    # path('logoutall/', knox_views.LogoutAllView.as_view(), name='api-logoutall'),

    path('a/', views.api_getAllEmp, name='apiemp'),
    # path('create', views.api_createEmp, name='create'),
    
    path('<id>/', views.api_getIDEmp, name='empID'),   
    path('update/<id>/', views.api_updateEmp, name='update-emp'),
    # path('delete/<id>/', views.api_delEmp, name='delete'),
    
    

]
