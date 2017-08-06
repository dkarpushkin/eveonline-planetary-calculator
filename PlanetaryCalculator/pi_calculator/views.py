from django.db.models import Count, F, Aggregate
from django.views import generic
from eve_database.models import InvGroup, InvType, PlanetSchematics


# def calculator_page(request):
#     return HttpResponse(loader.get_template('pi_calc.html').render())


class PiCalculaotorView(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        # группы планетарных материалов. 43 - id для planetary commodities
        groups = InvGroup.objects.filter(category__categoryId=43)#.prefetch_related('itemTypes')

        # schemas = PlanetSchematics.objects.annotate(typeGroupName=F(''))

        kwargs['planetCommodsGroups'] = groups

        return super().get(request, *args, **kwargs)
