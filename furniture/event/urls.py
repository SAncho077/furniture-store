from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news'),
    path('detail/<int:pk>/', views.news_detail, name='news-detail'),
]