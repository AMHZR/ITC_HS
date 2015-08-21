from django.views.generic import FormView
from forms import SearchForm


from haystack.generic_views import SearchView
from haystack.query import SearchQuerySet

import pysolr

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class HomePageView(SearchView):
    template_name = 'base.html'

class CustomPaginator(Paginator):

    def __init__(self, object_list, per_page, orphans=0,
                 allow_empty_first_page=True):
        self.sqs  = object_list
        self.object_list = object_list.docs
        self.per_page = int(per_page)
        self.orphans = int(orphans)
        self.allow_empty_first_page = allow_empty_first_page
        self._num_pages = self._count = None

    def _get_count(self):
        """
        Returns the total number of objects, across all pages.
        """
        if self._count is None:
            try:
                self._count = self.sqs.hits
            except (AttributeError, TypeError):
                self._count = len(self.object_list)
        return self._count
    count = property(_get_count)


class HSSearchView(FormView):
    template_name = 'index.html'
    solr = pysolr.Solr('http://localhost:8983/solr/hscode', timeout=10)
    form_class = SearchForm
    fq = []

    def __init__(self, *args, **kwargs):
        self.selected_facets = kwargs.pop("selected_facets", [])
        super(HSSearchView, self).__init__(*args, **kwargs)

    def get_initial(self):
        """
        Copies the get data and create the form initial data
        :return:
        """
        return self.request.GET.copy()

    def add_facet(self, field, solr_key):
        """

        :param field:
        :param solr_key:
        :return:
        """
        facet_join = ','.join
        if self.request.GET.getlist(field, ''):
            facet = []
            for value in self.request.GET.getlist(field, []):
                if value:
                    facet.append('"%s"'%(value))
            if len(facet):
                if facet and self.fq:
                    self.fq.append("{!tag=%s}%s:(%s)"%(solr_key,field,facet_join(facet)))
                else:
                    self.fq = ["{!tag=%s}%s:(%s)"%(solr_key,field,facet_join(facet))]
        return True

    def get_sqs(self):
        """
        Returns the search query set of solr
        :return:
        """
        data = self.request.GET.copy()
        keywords = data.get('keywords', '')
        if not keywords:
            keywords = '*:*'

        page_size = 15
        page = int(data.get('page',1))

        if page == 1:
            start = 0
        else:
            start = (page-1)*page_size
        params = {
            'hl': 'true',
            'rows':15,
            'start':start,
            'hl.fragsize': 8,
            'facet': 'on',
            'facet.field': ['{!ex=sec}section','{!ex=cpt}chapter','{!ex=art}article_exact',
                            'hs5_exact','hs6_exact','hs8_exact','{!ex=plc}policy_exact'],
            'facet.mincount': 1,
            'facet.query':[],
            'json.nl':'map',
            'spellcheck': 'true',
            'spellcheck.collate': 'true',
            'spellcheck.count': 1,
        }

        self.add_facet('section','sec')
        self.add_facet('chapter','cpt')
        self.add_facet('article_exact','art')
        self.add_facet('polict','plc')

        if len(self.fq):
            params['fq'] = self.fq

        if keywords:
            sqs = self.solr.search(keywords, **params)
            return sqs
        return ''


    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(form=form)

        sqs = self.get_sqs()

        context['sqs'] = sqs
        if sqs:
            paginator = CustomPaginator(sqs, 15)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                results = paginator.page(1)
            except EmptyPage:
                results = paginator.page(paginator.num_pages)
            context['results'] = results
        context['query'] = request.GET.copy()
        return self.render_to_response(context)