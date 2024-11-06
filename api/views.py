from django.shortcuts import render
from .models import Article,Author,Comment
from rest_framework import generics
from .serializers import UserSerializer,ArticleSerializer,CommentSerializer,AuthorSerializer


# Create your views here.

class UserListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
