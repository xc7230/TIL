from django.urls import path
from . import views

app_name = "index"

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name="new"),
    path('<int:que_id>/', views.detail, name="detail"),
    path('<int:que_id>/update/', views.update, name="update"),
    path('<int:que_id>/delete/', views.delete, name="delete"),
    path('<int:que_id>/survey/', views.survey, name="survey"),
    path('<int:sur_id>/vote', views.vote, name="vote"),
]