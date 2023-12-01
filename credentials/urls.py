from django.urls import path
from . import views
app_name='credentials'

urlpatterns = [
    path("register/",views.register,name="signup"),
    path("login/",views.login,name="signin"),
 
]
