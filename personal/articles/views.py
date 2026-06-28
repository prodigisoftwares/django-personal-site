from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from .forms import ArticleForm
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "articles/article_list.html"
    context_object_name = "articles"


class ArticleAddView(LoginRequiredMixin, View):
    def _get_context(self):
        return {
            "form": ArticleForm(),
        }

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "articles/article_add.html",
            self._get_context(),
        )

    def _save_article(self, form, request):
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        return article

    def _save_article_and_redirect(self, form, request):
        self._save_article(form, request)
        return HttpResponseRedirect(reverse("articles:article_list"))

    def _display_form_with_errors(self, form, request):
        return render(
            request,
            "articles/article_add.html",
            {"form": form},
        )

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            return self._save_article_and_redirect(form, request)
        else:
            return self._display_form_with_errors(form, request)
