from . import views
from django.urls import path
urlpatterns = [
      
      path('admin_signup/',views.admin_signup,name='admin_signup'),
      path('admin_signin/',views.admin_signin,name='admin_signin')
]