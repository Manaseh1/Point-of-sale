from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views
from .views import *

appname = 'accounts'

urlpatterns = [
    path('',home,name='home'),
    path('accounts/login/',views.signin,name='login'),
    path('profile/', views.profile, name='profile'),
    path('Lockscreen/', views.session_retrieval_view, name='lockscreen'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password-change'),
    path('password-change/done/', auth_views.PasswordChangeView.as_view(), name='password-change/done/'),
    path('password-reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password-reset/complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]