from django.urls import path

from .views import CommentIndexView, ShowCommentView, CreateCommentView, UpdateCommentView

app_name = 'comments'
urlpatterns = [
    path('', CommentIndexView.as_view(), name='allcomments'),
    path('<int:pk>/', ShowCommentView.as_view(), name='show'),
    path('create/', CreateCommentView.as_view(), name='create'),
    path('<int:pk>/update/', UpdateCommentView.as_view(), name='update'),
]
