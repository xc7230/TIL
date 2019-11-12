from django.urls import path
from . import views

urlpatterns = [
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('lotto/', views.lotto),
    path('lotto_result/', views.lotto_result),
    path('text/', views.text),
    path('text_result/', views.text_result),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('menu/', views.menu),
    path('subway/', views.subway),
    path('static_ex/', views.static_ex),
    path('index/', views.index),


]