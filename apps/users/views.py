from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created for {user.username}! Welcome to SkillCore.')
            return redirect('pricing:home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})
