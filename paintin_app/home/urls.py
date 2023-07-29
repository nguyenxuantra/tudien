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
    path('painting/<int:pk>/',views.painting_detail,name='painting_detail'),
    path('search_history/', views.search_history,name='search_history'),
    path('painting_list/', views.painting_list, name='painting_list'),
    path('add/', views.add_painting, name='add_painting'),
    path('edit/<int:pk>/', views.edit_painting, name='edit_painting'),
    path('delete/<int:pk>/', views.delete_painting, name='delete_painting'),
    path('report_issue/', views.report_issue, name='report_issue'),
]
