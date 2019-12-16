from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('<int:m_id>', views.detail, name="detail"),
    path('<int:m_id>/edit/', views.edit, name="edit"),
    path('<int:m_id>/delete/', views.delete, name="delete"),
    path('search/', views.search, name="search"),
    path('interest/', views.movie_sort, name="score"),
    path('popular/', views.movie_sort, name="audience"),
    path('genre/', views.movie_sort, name="genre"),
    
]