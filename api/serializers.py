from rest_framework import serializers
from .models import Author, Article, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
class AuthorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Author
        fields = ['id', 'user']

class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Article
        fields =['id', 'title', 'content', 'author']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    article = ArticleSerializer()
    class Meta:
        model = Comment
        fields =['id', 'user', 'article', 'content']