#!/usr/bin/env python
# encoding: utf-8




from haystack.forms import SearchForm
from django import forms
from blog.models import Article, Category


class BlogSearchForm(SearchForm):
    querydata = forms.CharField(required=True)

    def search(self):
        datas = super(BlogSearchForm, self).search()
        if not self.is_valid():
            return self.no_query_found()

        if self.cleaned_data['querydata']:
            print(self.cleaned_data['querydata'])
        return datas
