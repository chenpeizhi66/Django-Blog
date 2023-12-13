from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'users' # namespace

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('logout/', views.logout_view, name='logout'),
    path('editor_users/', views.editor_users, name='editor_users'),
]