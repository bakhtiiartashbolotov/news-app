from django.urls import path

from .views import ArticleAPIView

urlpatterns = [
    path("", ArticleAPIView.as_view(), name="article_list"),
]