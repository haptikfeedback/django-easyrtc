from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth.models import Group


@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

def register(request):
    errors = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if request.POST.get("is_teacher"):
                user.groups.add(Group.objects.get(name='teacher'))            
            login(request, user)
            return redirect('index')
        else:
            errors = form.error_messages
    else:
        form = SignUpForm()
    return render(request, 'accounts/register.html', {'form': form, "errors": errors})
