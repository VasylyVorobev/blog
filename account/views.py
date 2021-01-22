from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from .forms import RegisterForm
from django.shortcuts import render
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.urls import reverse_lazy
from posts.mixins import CustomSuccessMessageMixin


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            login(request, user)
            return HttpResponseRedirect('/')
        return render(request, 'registration/register.html', {'form': form})


class PasswordChange(CustomSuccessMessageMixin, PasswordChangeView):
    success_url = reverse_lazy('posts:post_list_url')
    success_msg = 'Пароль успешно изменен'


class PasswordReset(PasswordResetView):
    success_url = reverse_lazy('account:password_reset_done')
