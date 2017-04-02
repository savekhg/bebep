from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.core.urlresolvers import reverse

# Create your views here.
from web.models import CommonCodeTb
from colorpick.views import get_brand_list_data


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context = get_brand_list_data(context)

        return context


class BrandDetailView(TemplateView):
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super(BrandDetailView, self).get_context_data(**kwargs)
        context['ClassCommonCode'] = CommonCodeTb.objects.filter(upper_common_cd='01', group_cd=context['common_cd'],
                                                                 use='1').order_by('order')
        context = get_brand_list_data(context)

        return context
