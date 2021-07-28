from rest_framework import serializers
from .models import Players


class PlayersSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "player_Name",
            "position",
            "age",
            "team",
            "created_at",
            "author",
        )
        model = Players
