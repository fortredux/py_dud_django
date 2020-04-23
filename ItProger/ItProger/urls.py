"""ItProger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # Добавили include
from users import views as usersviews
from django.contrib.auth import views as authsviews

urlpatterns = [
    path('admin/', admin.site.urls),
    # Через include прописали путь к нашему blog\urls.py
    path('registration/', usersviews.register, name='registration'),
    path('user/', authsviews.LoginView.as_view(template_name='users/user.html'), name='user'),
    path('exit/', authsviews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
    path('', include('blog.urls')),
    # Так не работает, либо нужно было проходить по
    # http://127.0.0.1:8000/blog/empty,
    # либо создать новое приложение.
    # Путь path('', views.home, name='blog-home')
    # запускает функцию home из views.py
    # path('empty/', include('blog.urls'))
]
