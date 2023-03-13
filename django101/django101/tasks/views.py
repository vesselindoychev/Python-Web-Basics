from django.http import HttpResponse
from django.shortcuts import render

from django101.tasks.models import Task


# def home(request):
#     items = Task.objects.all()
#     item_strings = [f"<li>{t.title} - {t.text}</li>" for t in items]
#     items_string = ''.join(item_strings)
#     html = f'''
#         <h1>It works</h1>
#         {items_string}
#     '''
#     return HttpResponse(html)

def home(request):
    tasks = Task.objects.all()
    sorted_tasks = sorted(tasks, key=lambda x: x.title)
    context = {
        'title': 'It works from view!',
        'tasks': Task.objects.all(),
        'sorted_tasks': sorted_tasks
    }
    return render(request, 'home.html', context)