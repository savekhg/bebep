from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.core.urlresolvers import reverse

# Create your views here.
from web.models import CommonCodeTb
from django.shortcuts import get_object_or_404

class IndexView(TemplateView) :
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['ClassCommonCode'] = CommonCodeTb.objects.filter(upper_common_cd='01', group_cd='BZ', user='1').order_by('order')

        return context

class brandDetailView(TemplateView) :
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super(brandDetailView, self).get_context_data(**kwargs)
        context['ClassCommonCode'] = CommonCodeTb.objects.filter(upper_common_cd='01', group_cd=context['common_cd'],
                                                                 user='1').order_by('order')
        return context