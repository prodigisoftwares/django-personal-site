from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from articles.models import Article


class ArticleListViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.published = Article.objects.create(
            title="Published Article",
            content="Some content",
            author=self.user,
            is_published=True,
        )
        self.unpublished = Article.objects.create(
            title="Draft Article",
            content="Draft content",
            author=self.user,
            is_published=False,
        )
        self.url = reverse("articles:article_list")

    def test_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "articles/article_list.html")

    def test_context_contains_articles(self):
        response = self.client.get(self.url)
        self.assertIn("articles", response.context)

    def test_lists_all_articles(self):
        response = self.client.get(self.url)
        self.assertEqual(response.context["articles"].count(), 2)
