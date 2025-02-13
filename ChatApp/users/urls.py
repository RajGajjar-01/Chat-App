from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register_view, name='user-register'),
    path('logout/', views.logout_view, name='user-logout'),
    path('login/', auth_views.LoginView.as_view(template_name='users/Login.html'), name='login'),
]   


