from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('users/',views.change_password,name='users'),
    path('photos/',views.upload_photo,name='upload'),
    path('accounts/registration/',views.registration,name='register'),
    path('accounts/',views.logOutDash,name='LogOut'),
    path('deletephoto',views.deletePhoto,name='delete_photo')
]
