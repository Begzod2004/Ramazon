from rest_framework import serializers

from hududlar.models import Hududlar, Vaqt


class HududSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hududlar
        fields = '__all__'

class VaqtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaqt
        fields = '__all__'