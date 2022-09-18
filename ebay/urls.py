from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authAccepted/', views.authAccepted, name='authAccepted'),
    path('authDeclined/', views.authDeclined, name='authDeclined'),
    path('<str:user_token>/getUser/', views.getUser, name='getUser'),
    path('<str:user_token>/getMemberMessages/', views.getMemberMessages, name='getMemberMessages'),
    path('<str:user_token>/getOrders/', views.getOrders, name='getOrders'),
]