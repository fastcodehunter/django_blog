from django.shortcuts import render,redirect
from .forms import FormAuthorizationUser,ModelFormRegistrationsUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib import messages


def sing_in(request):
    if request.method == 'POST':
        form = FormAuthorizationUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect('list_blog')
    else:
        form = FormAuthorizationUser()
    return render(request, 'singin/login.html', {'form': form})
    






def sing_up(request):
    if request.method == 'POST':
        form = ModelFormRegistrationsUser(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            password=form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            return redirect('list_blog')
    else:
        form = ModelFormRegistrationsUser()
                # Получаем информацию о непрошедших валидациях
        error_messages = form.errors.values()
        # Выводим сообщения об ошибках
        for error in error_messages:
            messages.error(request, error)

    return render(request, 'singup/registration.html', {'form': form})
