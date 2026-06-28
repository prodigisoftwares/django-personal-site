from django.urls import path
from .views import ArticleAddView, ArticleListView

app_name = "articles"

urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list"),
    path("add/", ArticleAddView.as_view(), name="article_add"),
]
