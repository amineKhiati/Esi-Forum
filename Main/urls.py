from django.urls import path
from . import views


app_name = 'Main'


urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('edituser', views.dashboard_editProfile, name='edituser'),
    path('users', views.users, name='users'),
    path('login/', views.login_request, name='login'),
    path('home/', views.loggedin, name='home'),
    path('logout/', views.logout_request, name='logout'),
    path('usersettings/', views.editeProfile, name='editprofile'),

]