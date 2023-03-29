from django.shortcuts import render, redirect

from expenses_tracker.main.forms.expenses import CreateExpenseForm, EditExpenseForm, DeleteExpenseForm
from expenses_tracker.main.models import Expense


def show_create_expenses_view(request):
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show home with profile')
    else:
        form = CreateExpenseForm(request.FILES)

    context = {
        'form': form,
    }

    return render(request, 'expenses/expense-create.html', context)


def show_edit_expenses_view(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditExpenseForm(request.POST, request.FILES, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('show home with profile')
    else:
        form = EditExpenseForm(instance=expense)

    context = {
        'form': form,
        'expense': expense,
    }

    return render(request, 'expenses/expense-edit.html', context)


def show_delete_expenses_view(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteExpenseForm(request.POST, request.FILES, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('show home with profile')
    else:
        form = DeleteExpenseForm(instance=expense)

    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'expenses/expense-delete.html', context)
