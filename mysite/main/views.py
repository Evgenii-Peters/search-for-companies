from django.shortcuts import render

from .filler import find_firm_data
from .form import TaskForm


def create(request):
    if request.method == 'POST' and 'saveFormBtn' in request.POST:
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
    form = TaskForm()
    context = {
        'form': form
    }
    if request.method == 'POST' and 'fillFormBtn' in request.POST:
        form = TaskForm(request.POST or None)
        if form.is_valid():
            print("validation has occurred")
            result = TaskForm()
            inn = form.data["inn"]
            print("INN received")
            firm_data = find_firm_data(inn)
            print("A dictionary of values was obtained")
            result.__init__(firm_data)
            print("The data is entered in the form")
            form = result
        else:
            print("Валидация не прошла")
            form = TaskForm().data
        context = {
            'form': form
        }
    return render(request, 'index.html', context)
