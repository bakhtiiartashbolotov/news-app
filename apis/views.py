from rest_framework import generics 
from articles.models import Article
from .serializers import ArticleSerializer
class ArticleAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all() 
    serializer_class = ArticleSerializer
class ArticleDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all() 
    serializer_class = ArticleSerializer