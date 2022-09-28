from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authAccepted/', views.authAccepted, name='authAccepted'),
    path('authDeclined/', views.authDeclined, name='authDeclined'),
    path('<str:access_token>/getUser/', views.getUser, name='getUser'),
    path('<str:access_token>/getMemberMessages/', views.getMemberMessages, name='getMemberMessages'),
    path('<str:access_token>/<int:NumberOfDays>/getOrders/', views.getOrders, name='getOrders'),
]