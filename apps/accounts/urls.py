from django.urls import path
from . import views
#urls de la parte de login y creacion de usuarios
urlpatterns = [
    path('login/',views.login, name='login'),
    path('logout', views.logout,name='logout'),
    path('register/', views.register_user, name="register"),
]