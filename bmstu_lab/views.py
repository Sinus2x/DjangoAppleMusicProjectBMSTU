from django.shortcuts import render
from datetime import date
from bmstu_lab.models import Albums


def hello(request):
    return render(request, 'index.html', {'data': {
        'current_date': date.today(),
        'list': ['python', 'django', 'html']
    }})


def GetOrders(request):
    return render(request, 'orders.html', {'data': {
        'current_date': date.today(),
        'albums': Albums.objects.all()
    }})


def GetOrder(request, id):
    return render(request, 'order.html', {'data': {
        'current_date': date.today(),
        'album': Albums.objects.filter(album_id=id)
    }})
