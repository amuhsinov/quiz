from django.urls import path, include

from accounts.views import signup_user, user_profile, logout_user, signin_user

urlpatterns = [
    path('signup/', signup_user, name='signup user'),
    path('signin/', signin_user, name='signin user'),
    path('profile/', user_profile, name='user profile'),
    path('logout/', logout_user, name='logout user'),
    path('', include('django.contrib.auth.urls')),
]