from django.shortcuts import render
from datetime import date


def hello(request):
    return render(request, 'index.html', {'data': {
        'current_date': date.today(),
        'list': ['python', 'django', 'html']
    }})


def GetOrders(request):
    return render(request, 'orders.html', {'data' : {
        'current_date': date.today(),
        'artists': [
            {'title': 'AC/DC', 'id': 1},
            {'title': 'Nirvana', 'id': 2},
            {'title': 'Led Zeppelin', 'id': 3},
        ]
    }})


def GetOrder(request, id):
    return render(request, 'order.html', {'data' : {
        'current_date': date.today(),
        'id': id
    }})
