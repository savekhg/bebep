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
        context['ModelCommonCode'] = CommonCodeTb.objects.filter(upper_common_cd='01', group_cd=context['brand_cd'],
                                                                 use='1').order_by('order')

        for model_cd in context['ModelCommonCode']:
            model_cd.detail_model_cd = CommonCodeTb.objects.filter(upper_common_cd=model_cd.common_cd,
                                                                   use='1').order_by('order')

        context = get_brand_list_data(context)

        return context


class VehicleImgDetailView(TemplateView):
    template_name = 'vehicle_img_main.html'

    def get_context_data(self, **kwargs):
        context = super(VehicleImgDetailView, self).get_context_data(**kwargs)
        context = get_brand_list_data(context)

        return context
