from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.index),
    path('register/',views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('dangnhap/',views.dangnhap,name='dangnhap'),
    path('search/',views.search,name='search'),
    path('painting/<int:pk>/',views.painting_detail,name='painting_detail')
]
