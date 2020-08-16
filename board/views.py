from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from .forms import CommentForm
from .models import Comment

# Create your views here.


class CommentIndexView(ListView):
    model = Comment


class ShowCommentView(DetailView):
    model = Comment


class CreateCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy('comments:allcomments')
