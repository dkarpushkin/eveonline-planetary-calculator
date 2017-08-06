from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response

from eve_database.models import InvType, PlanetSchematics, InvCategories, InvGroup
from eve_database.serializers import InvTypeSerializer, PSchematicsSerializer, InvCategoriesSerializer, InvGroupSerializer


class InvTypesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InvType.objects.all()
    serializer_class = InvTypeSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset

        groupid = self.request.query_params.get('groupid', None)
        catid = self.request.query_params.get('catid', None)
        if groupid is not None:
            queryset = queryset.filter(group_id=groupid)
        elif catid is not None:
            queryset = queryset.filter(group__category__categoryId=catid)
        else:
            # выдаем только по фильтру. их слишком много
            raise Http404

        return Response(self.serializer_class(queryset, many=True, read_only=True).data)


class PSchematicsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PlanetSchematics.objects.all()
    serializer_class = PSchematicsSerializer

    def get_queryset(self):
        queryset = self.queryset

        outgroupid = self.request.query_params.get('outgroupid', None)
        ingroupid = self.request.query_params.get('ingroupid', None)

        if outgroupid is not None:
            queryset = queryset.filter(typeMaps__type__group_id=outgroupid, typeMaps__isinput__exact=False)
        elif ingroupid is not None:
            queryset = queryset.filter(typeMaps__type__group_id=ingroupid, typeMaps__isinput__exact=True).distinct()

        outtype = self.request.query_params.get('outtype', None)
        if outtype is not None:
            queryset = queryset.filter(typeMaps__type__typeID=outtype, typeMaps__isinput__exact=False).distinct()

        queryset.prefetch_related('typeMaps')

        return queryset


class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InvCategories.objects.all()
    serializer_class = InvCategoriesSerializer


class GroupsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InvGroup.objects.all()
    serializer_class = InvGroupSerializer

    def get_queryset(self):
        queryset = self.queryset

        catid = self.request.query_params.get('catid', None)
        if catid is not None:
            queryset = queryset.filter(category__categoryId=catid)

        return queryset
