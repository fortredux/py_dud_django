from django.urls import path

from . import views


urlpatterns = [
    path('', views.ShowNewsView.as_view(), name='blog-home'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/add/', views.CreateNewsView.as_view(), name='news-add'),
    path('news/<int:pk>/update/', views.UpdateNewsView.as_view(), name='news-update'),
    path('contacts/', views.contacts, name='blog-contacts'),
]
