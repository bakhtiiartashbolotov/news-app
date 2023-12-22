from django.urls import path

from .views import ArticleAPIView,ArticleDetails

urlpatterns = [
    path("", ArticleAPIView.as_view(), name="article_list"),
    path("<int:pk>/", ArticleDetails.as_view(), name="article_details"),

]