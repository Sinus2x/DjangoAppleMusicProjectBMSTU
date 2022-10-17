from bmstu_lab.models import Albums
from rest_framework import serializers


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Albums
        # Поля, которые мы сериализуем
        fields = ["pk", "artist", "name", "n_songs", "description", "img"]