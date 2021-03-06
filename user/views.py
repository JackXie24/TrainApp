from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserRegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})


@login_required
def dashborad(request):
    return render(request, 'index.html')


@login_required
def profile(request):
    return render(request, 'profile.html')
