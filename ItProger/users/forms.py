from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  # Это мы наследуем


class UserOurReistration(UserCreationForm):
    # requierd=True можно не писать - это занчание по умолчанию.
    email = forms.EmailField(required=True)
    
    class Meta:
        # Лектор говорит, что это тот самый User из импортов
        model = User
        # В таком порядке будет выводится формочки
        fields = ['username', 'email', 'password1', 'password2']
