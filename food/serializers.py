from rest_framework import serializers
from .models import Food, Comment, Reply


class FoodSerializer(serializers.ModelSerializer):
    '''def create(self, validated_data):
        return Food.objects.create(**validated_data)'''

    class Meta:
        model = Food
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    '''def create(self, validated_data):
        return Comment.objects.create(**validated_data)'''

    class Meta:
        model = Comment
        fields = '__all__'


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'''





