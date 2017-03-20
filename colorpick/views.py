from django.views.generic.base import TemplateView

# Create your views here.
from web.models import CommonCodeTb

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['brandCommonCode'] = CommonCodeTb.objects.filter(upper_common_cd='00', user='1').order_by('order')

        return context