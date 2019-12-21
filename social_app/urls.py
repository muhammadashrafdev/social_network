"""social_network URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import HomeView, create_post,correct_post,reject_post,approve_post,MyPostView,MyTaskView,PublicPostView



from django.urls import path
from django.contrib.auth import views as  auth_views
from django.contrib.auth.views import LoginView ,LogoutView ,PasswordChangeView ,PasswordChangeDoneView ,PasswordResetCompleteView,PasswordResetView, PasswordResetConfirmView ,PasswordResetDoneView
from django.contrib.auth import views

from django.urls import reverse_lazy

urlpatterns = [
    path('home/', HomeView.as_view(), name="home"),
    path('posts/', create_post, name="create_post"),
    path('myposts/',MyPostView.as_view,name="mypost"),
    path('mytasks/',MyTaskView.as_view,name="mytask"),
    path('public_posts/',PublicPostView.as_view,name="public_post"),
    path('reject/',reject_post,name="reject"),
    path('approve/',approve_post,name="approve"),
    path('correct/',correct_post,name="correct"),

    # Main websit page
    path('', HomeView.as_view(), name='home'),
    # create user with sign up form
    # path('signup/', ClientSignUpView.as_view(), name='signup'),
    # update client profile
    # path('signup/<int:pk>', ClientProfileUpdateView.as_view(), name='update_profile'),
    # Login
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='login.html'),
         name='login'),
    # Logout
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    # Main Dashboard
    # path('dashboard/', DashboardView.as_view(template_name='well_come_dashboard.html'), name='well_come_dashboard'),

    # Change Password
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='client/change-password.html',
            success_url='/'
        ),
        name='change_password'
    ),

    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='commons/password-reset/password_reset.html',
             subject_template_name='commons/password-reset/password_reset_subject.txt',
             email_template_name='commons/password-reset/password_reset_email.html',
             success_url=reverse_lazy('password_reset_done')
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='commons/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='commons/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='commons/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),

]
