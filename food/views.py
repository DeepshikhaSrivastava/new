from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from serializers import FoodSerializer,CommentSerializer, ReplySerializer
from rest_framework import viewsets
from rest_framework.decorators import detail_route,list_route
from .models import Food, Comment, Reply




class FoodViewSet(viewsets.ModelViewSet):

    serializer_class = FoodSerializer
    queryset = Food.objects.all()

    @detail_route(methods=['GET'])
    def comment(self, request, pk=None):
        comments = Comment.objects.filter(food_id=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    @list_route(methods=['GET'])
    def get_all_food(self, request):
        food = Food.objects.all()
        serializer = FoodSerializer(food, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    @detail_route(methods=['GET'])
    def reply(self, request, pk=None):
        replies = Reply.objects.filter(comment_id=pk)
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data)

    @list_route(methods=['GET'])
    def get_all_comment(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)


class ReplyViewSet(viewsets.ModelViewSet):

    serializer_class = ReplySerializer
    queryset = Reply.objects.all()




