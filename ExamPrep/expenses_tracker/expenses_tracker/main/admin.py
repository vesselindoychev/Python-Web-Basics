from django.contrib import admin

from expenses_tracker.main.models import Profile, Expense


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    pass