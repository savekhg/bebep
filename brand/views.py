from django.views.generic.base import TemplateView

# Create your views here.


class IndexView(TemplateView):
    template_name = 'brand/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        return context
