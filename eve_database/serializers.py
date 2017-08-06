from .models import InvType, PlanetSchematics, PlanetSchematicsTypeMap, InvCategories, InvGroup
from rest_framework import serializers


class InvCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvCategories


class InvGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvGroup


class InvTypeSchematicsMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetSchematicsTypeMap


class InvTypeSerializer(serializers.ModelSerializer):
    # schema = serializers.SerializerMethodField('get_schema_id', read_only=True)

    class Meta:
        model = InvType
        exclude = ('description', )


class PSchematicsTypeMapSerializer(serializers.ModelSerializer):
    type = InvTypeSerializer(read_only=True)

    class Meta:
        model = PlanetSchematicsTypeMap
        exclude = ('schematic', )


class PSchematicsSerializer(serializers.ModelSerializer):
    inputTypes = serializers.SerializerMethodField('get_input_types', read_only=True)
    outputType = serializers.SerializerMethodField('get_output_type', read_only=True)

    def get_input_types(self, schema):
        return PSchematicsTypeMapSerializer(schema.typeMaps.filter(isinput=True), many=True).data

    def get_output_type(self, schema):
        return PSchematicsTypeMapSerializer(schema.typeMaps.filter(isinput=False).first()).data

    class Meta:
        model = PlanetSchematics
        exclude = ('types',)
