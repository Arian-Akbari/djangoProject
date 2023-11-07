from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    contex = {
        'name': 'patrik',
        'age': '23',
        'nationality': 'iran'

    }
    name = 'reza'
    name2 = 'patrik'
    return render(request, 'index.html', contex)


def counter(request):
    text = request.POST['text']
    amount = len(text.split())
    print(amount)
    return render(request, 'counter.html', {'amount': amount})
