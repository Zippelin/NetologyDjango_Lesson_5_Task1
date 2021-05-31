from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'

    articels = Article.objects.all().prefetch_related('scopes').order_by(ordering)
    context = {'object_list': articels}

    return render(request, template, context)
