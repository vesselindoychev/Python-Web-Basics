from django.shortcuts import render, redirect

from expenses_tracker.main.helpers import get_profile, get_money_left
from expenses_tracker.main.models import Expense


def show_home_with_profile(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    if profile:
        money_left = get_money_left()
    else:
        money_left = 0

    context = {
        'profile': profile,
        'expenses': expenses,
        'money_left': money_left,
    }
    if not profile:
        return redirect('create profile page')
    return render(request, 'home-with-profile.html', context)