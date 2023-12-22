from django.views.generic import ListView, DetailView # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView # new 
from django.urls import reverse_lazy

from apis.serializers import ArticleSerializer # new
from .models import Article
from rest_framework import generics

class ArticleListView(ListView): 
    model = Article
    template_name = "article_list.html"
class ArticleDetailView(DetailView): # new 
    model = Article
    template_name = "article_detail.html"
class ArticleUpdateView(UpdateView): # new
    model = Article
    fields = (
        "title",
"body", )
    template_name = "article_edit.html"
class ArticleDeleteView(DeleteView): # new 
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")
class ArticleCreateView(CreateView): # new 
    model = Article
    template_name = "article_new.html"
    fields = (
        "title",
        "body",
        "author",
)
# CRUD with REST APIs
class ArticleList(generics.ListCreateAPIView): 
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer