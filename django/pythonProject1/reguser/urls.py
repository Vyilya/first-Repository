from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginUserView, name='loginUser'),
    path('reguser/', views.reguserView, name='reguser'),

]
