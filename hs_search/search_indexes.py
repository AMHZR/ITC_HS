__author__ = 'aamir'

import datetime
from haystack import indexes
from .models import hscode as HsCode


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    section = indexes.CharField(faceted=True)
    chapter = indexes.CharField(faceted=True)

    article = indexes.CharField(faceted=True)
    hs = indexes.CharField(model_attr='hs')
    id = indexes.CharField(model_attr='hs')
    desc = indexes.CharField(model_attr='desc')
    policy = indexes.CharField(faceted=True)
    hs5 = indexes.CharField(model_attr='hs_5', faceted=True)
    hs6 = indexes.CharField(model_attr='hs_6', faceted=True)
    hs8 = indexes.CharField(model_attr='hs_8', faceted=True)
    condition = indexes.CharField(model_attr='condition')

    def get_model(self):
        return HsCode

    def prepare_section(self, obj):
        return obj.article.chapter.section.name.strip()

    def prepare_chapter(self, obj):
        return obj.article.chapter.name.strip()

    def prepare_article(self, obj):
        return obj.article.heading.strip()

    def prepare_policy(self, obj):
        return obj.policy.strip()

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()