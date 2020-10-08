from django.urls import path
from . import views
urlpatterns = [
    path('', views.Post_list, name='Post_list'),
     path('Post/<int:pk>/', views.Post_detail, name='Post_detail'),
]