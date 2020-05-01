from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import News


def home(request):
    data = {
        'news': News.objects.all(),
        'title': 'Главная страница блога',
    }
    return render(request, 'blog/home.html', data)


class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']

    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Главная страница блога'
        return ctx


class NewsDetailView(DetailView):
    model = News
    print(model.title)
    # template_name = 'blog/news_detail.html'  # it's default value
    context_object_name = 'post'  # object by default

    def get_context_data(self, **kwards):
        ctx = super(DetailView, self).get_context_data(**kwards)
        ctx['title'] = News.objects.filter(pk=self.kwargs['pk']).first()
        return ctx


class CreateNewsView(CreateView):
    model = News
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def contacts(request):
    return render(request, 'blog/contacts.html', {'title': 'Страница о нас'})


def main(request):
    return render(request, 'blog/main.html', {'title': 'Main страница'})


def bootstrap(request):
    return render(request, 'blog/bootstrap.html', {'title': 'Bootstrap страница'})
