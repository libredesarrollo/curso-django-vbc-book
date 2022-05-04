from django.shortcuts import render

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView

class UserLoginView(LoginView):
    template_name="user/login.html"
    next_page="/book/management/index/"
    redirect_authenticated_user=True
    extra_context={
        'key1':"valor 1",
        'key2':"valor 2",
    }

class UserLogoutView(LogoutView):
    template_name="user/logout.html"
    next_page="/user/login"

class UserPasswordChangeView(PasswordChangeView):
    template_name="user/password/change.html"
    next_page="/user/login"

class UserPasswordResetView(PasswordResetView):
    template_name="user/password/reset.html"

