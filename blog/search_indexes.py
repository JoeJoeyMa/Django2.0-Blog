#!/usr/bin/env python
# encoding: utf-8



from haystack import indexes
from django.conf import settings
from blog.models import Article, Category, Tag


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    # title = indexes.CharField(document=True, use_template=True)
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(status='p')


"""
class CategoryIndex(indexes.SearchIndex, indexes.Indexable):
    name = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(status='p')
"""
