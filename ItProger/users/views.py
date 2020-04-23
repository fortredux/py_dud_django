from django.shortcuts import render, redirect  # redirect добавили в части 7
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserOurReistration

def register(request):
    if request.method == 'POST':
        form = UserOurReistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} был успешно создан, /'
                                      f'введите имя пользователя и пароль для авторизации')
            return redirect('user')
    else:
        form = UserOurReistration()
    return render(request, 'users/registration.html', {'form': form, 'title': 'Регистрация пользователя'})


@login_required
def profile(request):
    return render(request, 'users/profile.html')