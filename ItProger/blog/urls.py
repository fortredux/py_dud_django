from django.urls import path
# Ипортируем из текущей папки
from . import views

# Добавили функцию из views.py текущей папки
# Мы прописали в urls.py проекта ItProger, что ссылка
# http://127.0.0.1:8000/blog/ вызывает функцию home
# из файла views.py приложения blog.
urlpatterns = [
    # Это значит, что при вызове просто blog, '' в следующей записи,
    # мы выполним функцию home. А вот если допишем дальше /empty, то
    # вызовем функцию empty из файла views.
    path('', views.home, name='blog-home'),
    path('contacts/', views.contacts, name='blog-contacts'),
    path('bootstrap/', views.bootstrap, name='blog-bootstrap'),
]
