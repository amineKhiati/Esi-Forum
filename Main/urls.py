from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentUpdateView,
)




urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('edituser', views.dashboard_editProfile, name='edituser'),
    path('users', views.users, name='users'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('usersettings/', views.editeProfile, name='editprofile'),
    path('searchresults/',views.search, name='search'),
    path('userpage/',views.userpage, name='userpage'),
    path('engpub/<int:pk>',views.enrigstre_pub,name='engpub'),
    path('reports/',views.ReportListView.as_view(),name='reports'),
    path('reports/delete/<int:pk>',views.ReportDeleteView.as_view(),name='report-delete'),
    path('reports/deletemeesage/<int:pk>',views.MessageDeleteView.as_view(),name='message-delete'),
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/new/', views.add_comment_to_post, name='comment-new'),
    path('post/<int:pk1>/comment/delete/<int:pk2>/', views.comment_remove, name='comment-delete'),
    path('post/<int:pk1>/comment/update/<int:pk2>/', views.comment_update, name='comment-update'),
    
]