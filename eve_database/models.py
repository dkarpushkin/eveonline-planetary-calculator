# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

import django.db.models.options as options
from django.db.models import F

options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('db_name',)


class InvCategories(models.Model):
    categoryId = models.BigIntegerField(db_column='categoryID', primary_key=True)  # Field name made lowercase.
    categoryName = models.TextField(db_column='categoryName', blank=True, null=True)  # Field name made lowercase.
    iconid = models.BigIntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    published = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'invCategories'


class InvGroup(models.Model):
    groupId = models.BigIntegerField(db_column='groupID', primary_key=True)  # Field name made lowercase.
    # categoryid = models.BigIntegerField(db_column='categoryID', blank=True, null=True)  # Field name made lowercase.
    category = models.ForeignKey(InvCategories, db_column='categoryID', blank=True, null=True,
                                 related_name='groups')
    groupName = models.TextField(db_column='groupName', blank=True, null=True)  # Field name made lowercase.
    iconid = models.BigIntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    useBasePrice = models.NullBooleanField(db_column='useBasePrice')  # Field name made lowercase.
    anchored = models.NullBooleanField()
    anchorable = models.NullBooleanField()
    fittablenonsingleton = models.NullBooleanField(db_column='fittableNonSingleton')  # Field name made lowercase.
    published = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'invGroups'

    def types_with_schemaId(self):
        return self.itemTypes.filter(piSchematicMaps__isinput=False)\
            .annotate(schemaId=F('piSchematics'))


class InvMarketGroup(models.Model):
    marketGroupId = models.BigIntegerField(db_column='marketGroupID', unique=True)  # Field name made lowercase.
    parentGroupId = models.BigIntegerField(db_column='parentGroupID', blank=True, null=True)  # Field name made lowercase.
    marketGroupName = models.TextField(db_column='marketGroupName', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    iconid = models.BigIntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    hasTypes = models.NullBooleanField(db_column='hasTypes')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invMarketGroups'


class InvType(models.Model):
    typeID = models.IntegerField(db_column='typeID', primary_key=True)  # Field name made lowercase.
    group = models.ForeignKey(InvGroup, db_column='groupID', blank=True, null=True,
                              related_name='itemTypes')
    typeName = models.TextField(db_column='typeName', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    mass = models.TextField(blank=True, null=True)  # This field type is a guess.
    volume = models.TextField(blank=True, null=True)  # This field type is a guess.
    capacity = models.TextField(blank=True, null=True)  # This field type is a guess.
    portionSize = models.IntegerField(db_column='portionSize', blank=True, null=True)  # Field name made lowercase.
    raceid = models.IntegerField(db_column='raceID', blank=True, null=True)  # Field name made lowercase.
    baseprice = models.TextField(db_column='basePrice', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    published = models.IntegerField(blank=True, null=True)
    marketGroup = models.ForeignKey(InvMarketGroup, db_column='marketGroupID', blank=True, null=True,
                                    related_name='itemTypes')
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    soundid = models.IntegerField(db_column='soundID', blank=True, null=True)  # Field name made lowercase.
    graphicid = models.BigIntegerField(db_column='graphicID', blank=True, null=True)  # Field name made lowercase.

    # piSchematics = ManyToMany(PlanetSchematics)
    # producedSchmatics = ManyToMany(PlanetSchematics)    # для фабрик

    # piSchematicMaps = ManyToOne(PlanetSchematicsTypeMap)  # промежуточная таблица на piSchematics

    class Meta:
        managed = False
        db_name = 'eve_db'
        db_table = 'invTypes'

    def __unicode__(self):
        return self.typeName

    def __str__(self):
        return self.typeName

    def get_producing_pi_schematics(self):
        # schMap = self.piSchematicMaps.filter(isinput=False)
        sch_map = self.piSchematics.filter(types__piSchematicMaps__isinput=False)

        return sch_map.first()


class PlanetSchematics(models.Model):
    schematicID = models.IntegerField(db_column='schematicID', primary_key=True)  # Field name made lowercase.
    schematicName = models.TextField(db_column='schematicName', blank=True, null=True)  # Field name made lowercase.
    cycleTime = models.IntegerField(db_column='cycleTime', blank=True, null=True)  # Field name made lowercase.

    types = models.ManyToManyField(InvType, through='PlanetSchematicsTypeMap',
                                   related_name='piSchematics')
    factories = models.ManyToManyField(InvType, through='PlanetSchematicsPinMap',
                                       related_name='producedSchmatics')

    class Meta:
        db_name = 'eve_db'
        db_table = 'planetSchematics'

    def __unicode__(self):
        return self.schematicName

    def __str__(self):
        return self.schematicName

    def output_item_type(self):
        return self.itemTypeMap.filter(isinput=0).first().type

    def input_item_types(self):
        return [type.type for type in self.itemTypeMap.filter(isinput=1)]

    def getdict(self, **kwargs):
        result = dict(
            schematicId=self.schematicID,
            schematicName=self.schematicName,
            cycleTime=self.cycleTime,
        )

        if kwargs.get('extended_inputs', False):
            result['input'] = [{'type': t.type.getdict(extended_schematics=False), 'quantity': t.quantity}
                               for t in self.itemTypeMap.filter(isinput=True)]
        else:
            result['input'] = [{'typeId': t.type_id, 'typeName': t.type.typeName, 'quantity': t.quantity}
                               for t in self.itemTypeMap.filter(isinput=True)]

        out = self.itemTypeMap.filter(isinput=0).first()
        if kwargs.get('extended_output', False):
            result['output'] = {'type': out.type.getdict(extended_schematics=False), 'quantity': out.quantity}
        else:
            result['outputQuantity'] = out.quantity

        return result


class PlanetSchematicsPinMap(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    schematic = models.ForeignKey(PlanetSchematics, db_column='schematicID',
                                  related_name='schematicsPinMaps')#, primary_key=True)
    pinType = models.ForeignKey(InvType, db_column='pinTypeID',
                                related_name='schematicsPinMaps')#, primary_key=True)

    class Meta:
        db_name = 'eve_db'
        db_table = 'planetSchematicsPinMap'
        unique_together = (('schematic', 'pinType'),)


class PlanetSchematicsTypeMap(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    quantity = models.IntegerField()
    isinput = models.NullBooleanField(db_column='isInput', blank=True, null=True)  # Field name made lowercase.

    schematic = models.ForeignKey(PlanetSchematics, models.CASCADE,
                                  db_column='schematicID',
                                  related_name='typeMaps')#, primary_key=True)
    type = models.ForeignKey(InvType, models.CASCADE,
                             db_column='typeID',
                             related_name='piSchematicMaps')#, primary_key=True)

    class Meta:
        db_name = 'eve_db'
        db_table = 'planetSchematicsTypeMap'
        unique_together = (('schematic', 'type'),)


class Translationtables(models.Model):
    sourcetable = models.CharField(db_column='sourceTable', primary_key=True, max_length=200)  # Field name made lowercase.
    destinationtable = models.CharField(db_column='destinationTable', max_length=200, blank=True, null=True)  # Field name made lowercase.
    translatedkey = models.CharField(db_column='translatedKey', primary_key=True, max_length=200)  # Field name made lowercase.
    tcgroupid = models.IntegerField(db_column='tcGroupID', blank=True, null=True)  # Field name made lowercase.
    tcid = models.IntegerField(db_column='tcID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_name = 'eve_db'
        db_table = 'translationTables'
        unique_together = (('sourcetable', 'translatedkey'),)


class Trntranslationcolumns(models.Model):
    tcgroupid = models.IntegerField(db_column='tcGroupID', blank=True, null=True)  # Field name made lowercase.
    tcid = models.IntegerField(db_column='tcID', primary_key=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='tableName', max_length=256)  # Field name made lowercase.
    columnname = models.CharField(db_column='columnName', max_length=128)  # Field name made lowercase.
    masterid = models.CharField(db_column='masterID', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_name = 'eve_db'
        db_table = 'trnTranslationColumns'


class Trntranslationlanguages(models.Model):
    numericlanguageid = models.IntegerField(db_column='numericLanguageID', primary_key=True)  # Field name made lowercase.
    languageid = models.CharField(db_column='languageID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    languagename = models.CharField(db_column='languageName', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_name = 'eve_db'
        db_table = 'trnTranslationLanguages'


class Trntranslations(models.Model):
    tcid = models.IntegerField(db_column='tcID', primary_key=True)  # Field name made lowercase.
    keyid = models.IntegerField(db_column='keyID', primary_key=True)  # Field name made lowercase.
    languageid = models.CharField(db_column='languageID', primary_key=True, max_length=50)  # Field name made lowercase.
    text = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_name = 'eve_db'
        db_table = 'trnTranslations'
        unique_together = (('tcid', 'keyid', 'languageid'),)
