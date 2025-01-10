from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from .forms import UserForm

# Регистрация пользователя
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users_list')
    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})

# Список всех пользователей
def users_list(request):
    users = UserProfile.objects.all()
    return render(request, 'accounts/users_list.html', {'users': users})

# Страничка конкретного пользователя
def user_detail(request, user_id):
    user = get_object_or_404(UserProfile, id=user_id)
    return render(request, 'accounts/user.html', {'user': user})