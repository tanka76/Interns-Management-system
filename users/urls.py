from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import LogoutView


app_name = 'users'

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),

]