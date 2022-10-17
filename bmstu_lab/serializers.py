from bmstu_lab.models import Albums, Customers, Orders, AlbumsOrders
from rest_framework import serializers


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Albums
        # Поля, которые мы сериализуем
        fields = ["pk", "artist", "name", "n_songs", "description", "img"]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Customers
        # Поля, которые мы сериализуем
        fields = ["pk", "name", "phone", "email"]


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer

    class Meta:
        # Модель, которую мы сериализуем
        model = Orders
        # Поля, которые мы сериализуем
        fields = ["pk", "creation_date", "edit_date", "exec_date"]


class AlbumOrderSerializer(serializers.ModelSerializer):
    order = OrderSerializer
    coffee = AlbumSerializer

    class Meta:
        # Модель, которую мы сериализуем
        model = AlbumsOrders
        # Поля, которые мы сериализуем
        fields = ["order", "album"]