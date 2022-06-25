from django.urls import path

from .import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('p/',views.profile,name='prof'),
    path('s',views.Show_profile,name='so'),
    path('p/<int:id>/',views.profile,name='edit'),
    path('wip',views.wip)
]
