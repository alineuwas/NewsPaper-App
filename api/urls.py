from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserListView.as_view(), name='users'),
    path('articles/',views.ArticleListView.as_view(),name='articles'),
    path('comments/',views.CommentListView.as_view(),name='comments'),
]