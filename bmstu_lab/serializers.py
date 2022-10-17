from bmstu_lab.models import Albums, Customers
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