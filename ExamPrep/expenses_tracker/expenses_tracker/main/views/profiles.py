from django.shortcuts import render, redirect

from expenses_tracker.main.forms.profiles import CreateProfileForm, EditProfileForm, DeleteProfileForm
from expenses_tracker.main.helpers import get_profile, get_money_left
from expenses_tracker.main.models import Expense


def show_profile(request):
    profile = get_profile()
    items = Expense.objects.count()
    money_left = get_money_left()
    context = {
        'profile': profile,
        'items': items,
        'money_left': money_left,
    }

    return render(request, 'profiles/profile.html', context)


def show_create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show home with profile')
    else:
        form = CreateProfileForm(request.FILES)

    context = {
        'form': form,
    }

    return render(request, 'profiles/home-no-profile.html', context)


def show_edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile page')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profiles/profile-edit.html', context)


def show_delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show home with profile')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profiles/profile-delete.html', context)
