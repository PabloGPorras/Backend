from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authAccepted/', views.authAccepted, name='authAccepted'),
    path('authDeclined/', views.authDeclined, name='authDeclined'),
    path('<str:code>/getUser/', views.getUser, name='getUser'),
    path('<str:user_token>/getMemberMessages/', views.getMemberMessages, name='getMemberMessages'),
    path('<str:code>/<int:NumberOfDays>/getOrders/', views.getOrders, name='getOrders'),
]