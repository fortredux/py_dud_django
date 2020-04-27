# Метод render позволяет вывести что либо на экран
from django.shortcuts import render
# Это будем ипользовать на время, до использования templates
# from django.http import HttpResponse
from .models import News

'''
news = [
    {
        'title': 'Наша первая запись',
        'text': 'Текст 1',
        'date': '1997',
        'author': 'Косс'
    },
    {
        'title': 'Наша вторая запись',
        'text': 'Текст 8',
        'date': '1998'
    }
]
'''


# Для всех функций здесь обязательный параметр request
def home(request):
    data = {
        'news': News.objects.all(),
        'title': 'Главная страница блога',
    }
    # Здесь нужно вернуть некую html разметку
    return render(request, 'blog/home.html', data)


# Создав функцию наподобие первой и прописав путь к ней в urls.py,
# я получил в ответ вызов функции home, а не этой!
# Достучаться можно по http://127.0.0.1:8000/blog/empty/
def contacts(request):
    # Третим аргументом можно передать ключевые аргументы
    return render(request, 'blog/contacts.html', {'title': 'Страница о нас'})


def main(request):
    return render(request, 'blog/main.html', {'title': 'Main страница'})


def bootstrap(request):
    return render(request, 'blog/bootstrap.html', {'title': 'Bootstrap страница'})
