from django.urls import path
from . import views

app_name='saas_app'

urlpatterns = [
    path("index/",views.demo,name="demos"),
 
]
