from django.urls import path
from . import views
from .views import user_password_reset, user_password_reset_sent, user_password_reset_confirm, user_password_reset_complete


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('users/', views.user_list, name='users'),
    path('settings/', views.user_settings, name='settings'),
    # user password reset
    path('password_reset/', user_password_reset.as_view(), name='password_reset'),
    path('password_reset_sent/', user_password_reset_sent.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', user_password_reset_confirm.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', user_password_reset_complete.as_view(), name='password_reset_complete'),
]
