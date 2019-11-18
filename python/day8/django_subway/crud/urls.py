from django.urls import path
from . import views


app_name ="crud"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('<int:pk>/article/', views.detail, name="article"),
    path('<int:pk>/update/', views.update, name="update"),
    # crud/pk/revise/ 최종 업데이트
    path('<int:pk>/revise/', views.revise, name="revise"),
    # crud/pk/delete/ 삭제하기
    path('<int:pk>/delete/', views.delete, name="delete"),

]