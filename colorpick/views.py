from django.views.generic.base import TemplateView

# Create your views here.
from web.models import CommonCodeTb


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context = get_brand_list_data(context)

        return context


class TestView(TemplateView):
    template_name = 'test.html'

    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)
        return context


def get_brand_list_data(context):
    context['BrandCommonCode'] = CommonCodeTb.objects.filter(upper_common_cd='00', use='1').order_by('order')

    return context
