from django.urls import path
from accounts import views
from .views import *

appname = 'accounts'

urlpatterns = [
    path('',home,name='home'),
<<<<<<< HEAD
    path('login/',signin,name='login'),
    path('password-change/')
=======
    path('Login/',signin,name='login'),
>>>>>>> 1ea3eec86982ddd4258e2c17a564dcb525e2908e
]