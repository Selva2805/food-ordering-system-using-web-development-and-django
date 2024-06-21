from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('checkout/', views.checkout, name='checkout'),
    path('order/', views.order, name='order'),
    path('homepage/', views.homepage, name='homepage'),
    path('logout/', views.logout, name='logout'),
]
