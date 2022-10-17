from django.shortcuts import render
from datetime import date
from rest_framework import viewsets
from bmstu_lab.serializers import AlbumSerializer, CustomerSerializer, AlbumOrderSerializer, OrderSerializer
from bmstu_lab.models import Albums, Customers, Orders


class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Albums.objects.all().order_by('name')
    serializer_class = AlbumSerializer  # Сериализатор для модели


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Customers.objects.all().order_by('name')
    serializer_class = CustomerSerializer  # Сериализатор для модели


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Orders.objects.all().order_by('pk')
    serializer_class = OrderSerializer  # Сериализатор для модели


def hello(request):
    return render(request, 'index.html', {'data': {
        'current_date': date.today(),
        'list': ['python', 'django', 'html']
    }})


def get_orders(request):
    return render(request, 'albums.html', {'data': {
        'current_date': date.today(),
        'albums': Albums.objects.all()
    }})


def get_order(request, id):
    return render(request, 'album.html', {'data': {
        'current_date': date.today(),
        'album': Albums.objects.filter(album_id=id)[0]
    }})
