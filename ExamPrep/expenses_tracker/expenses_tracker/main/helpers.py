from expenses_tracker.main.models import Profile, Expense


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def get_money_left():
    profile = get_profile()
    expenses = Expense.objects.all()
    total_sum = sum([expense.price for expense in expenses])
    money_left = profile.budget - total_sum
    return money_left
