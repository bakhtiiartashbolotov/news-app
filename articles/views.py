from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import ListView, DetailView, FormView # new
from django.views.generic.detail import SingleObjectMixin # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse # new

from apis.serializers import ArticleSerializer
from articles.forms import CommentForm # new
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
class ArticleDetailView(LoginRequiredMixin, View): # new
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)
class CommentGet(DetailView): # new
    model = Article
    template_name = "article_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context
class CommentPost(SingleObjectMixin, FormView): # new
    model = Article
    form_class = CommentForm
    template_name = "article_detail.html"
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.save()
        return super().form_valid(form)
    def get_success_url(self):
        article = self.get_object()
        return reverse("article_detail", kwargs={"pk": article.pk})
# CRUD with REST APIs
class ArticleList(generics.ListCreateAPIView): 
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer