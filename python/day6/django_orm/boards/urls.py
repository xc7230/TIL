from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('menu/', views.menu),
    path('subway/', views.subway),
    path('result_sub/<int:number>', views.result_sub),

]