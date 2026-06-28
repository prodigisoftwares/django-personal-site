from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from articles.models import Article


class ArticleAddViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="testuser", password="password")
        cls.url = reverse("articles:article_add")

    def setUp(self):
        self.client.login(username="testuser", password="password")

    def test_get_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_get_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "articles/article_add.html")

    def test_get_context_contains_form(self):
        response = self.client.get(self.url)
        self.assertIn("form", response.context)

    def test_post_valid_data_creates_article(self):
        self.client.post(
            self.url,
            {"title": "New Article", "content": "Body text", "is_published": False},
        )
        self.assertEqual(Article.objects.count(), 1)

    def test_post_valid_data_redirects_to_article_list(self):
        response = self.client.post(
            self.url,
            {"title": "New Article", "content": "Body text", "is_published": False},
        )
        self.assertRedirects(response, reverse("articles:article_list"))

    def test_post_valid_data_sets_author(self):
        self.client.post(
            self.url,
            {"title": "New Article", "content": "Body text", "is_published": False},
        )
        article = Article.objects.first()
        self.assertEqual(article.author, self.user)

    def test_post_invalid_data_does_not_create_article(self):
        self.client.post(
            self.url,
            {"title": "", "content": "", "is_published": False},
        )
        self.assertEqual(Article.objects.count(), 0)

    def test_post_invalid_data_rerenders_form_with_errors(self):
        response = self.client.post(
            self.url, {"title": "", "content": "", "is_published": False}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "articles/article_add.html")
        self.assertTrue(response.context["form"].errors)
