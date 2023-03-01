from rest_framework import serializers

from hududlar.models import *


class HududSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hududlar
        fields = '__all__'

class VaqtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaqt
        fields = '__all__'


class ViloyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viloyat
        fields = ('id', 'nomi', 'vaqt_farqi',)

class NamozVaqtiSerializer(serializers.ModelSerializer):
    class Meta:
        model = NamozVaqti
        fields = '__all__'
        



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'text', 'is_correct')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ('id', 'text', 'answers')


class VideoCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCategory
        fields = "__all__"

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"
