from django.urls import path
from . import views
urlpatterns = [
    
    path(r'', views.index, name='index'),
    # path(r'login/',views.login,name='login'),
    # path(r'loginresponse/',views.loginresponse,name='loginresponse'),
    # path(r'loginValidate/',views.loginValidate,name='loginValidate'),
    # path(r'contact',views.contact,name='contact')
]