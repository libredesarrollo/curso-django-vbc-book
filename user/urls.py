from django.urls import path

from .views import UserLoginView, UserLogoutView, UserPasswordChangeView,UserPasswordResetView

urlpatterns = [
    path('login',UserLoginView.as_view()),
    path('logout',UserLogoutView.as_view()),
    path('password-change',UserPasswordChangeView.as_view()),
    path('password-reset',UserPasswordResetView.as_view())
]