# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-06 15:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InvCategories',
            fields=[
                ('categoryId', models.BigIntegerField(db_column='categoryID', primary_key=True, serialize=False)),
                ('categoryName', models.TextField(blank=True, db_column='categoryName', null=True)),
                ('iconid', models.BigIntegerField(blank=True, db_column='iconID', null=True)),
                ('published', models.NullBooleanField()),
            ],
            options={
                'db_table': 'invCategories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InvGroup',
            fields=[
                ('groupId', models.BigIntegerField(db_column='groupID', primary_key=True, serialize=False)),
                ('groupName', models.TextField(blank=True, db_column='groupName', null=True)),
                ('iconid', models.BigIntegerField(blank=True, db_column='iconID', null=True)),
                ('useBasePrice', models.NullBooleanField(db_column='useBasePrice')),
                ('anchored', models.NullBooleanField()),
                ('anchorable', models.NullBooleanField()),
                ('fittablenonsingleton', models.NullBooleanField(db_column='fittableNonSingleton')),
                ('published', models.NullBooleanField()),
            ],
            options={
                'db_table': 'invGroups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InvMarketGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marketGroupId', models.BigIntegerField(db_column='marketGroupID', unique=True)),
                ('parentGroupId', models.BigIntegerField(blank=True, db_column='parentGroupID', null=True)),
                ('marketGroupName', models.TextField(blank=True, db_column='marketGroupName', null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('iconid', models.BigIntegerField(blank=True, db_column='iconID', null=True)),
                ('hasTypes', models.NullBooleanField(db_column='hasTypes')),
            ],
            options={
                'db_table': 'invMarketGroups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InvType',
            fields=[
                ('typeID', models.IntegerField(db_column='typeID', primary_key=True, serialize=False)),
                ('typeName', models.TextField(blank=True, db_column='typeName', null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('mass', models.TextField(blank=True, null=True)),
                ('volume', models.TextField(blank=True, null=True)),
                ('capacity', models.TextField(blank=True, null=True)),
                ('portionSize', models.IntegerField(blank=True, db_column='portionSize', null=True)),
                ('raceid', models.IntegerField(blank=True, db_column='raceID', null=True)),
                ('baseprice', models.TextField(blank=True, db_column='basePrice', null=True)),
                ('published', models.IntegerField(blank=True, null=True)),
                ('iconid', models.IntegerField(blank=True, db_column='iconID', null=True)),
                ('soundid', models.IntegerField(blank=True, db_column='soundID', null=True)),
                ('graphicid', models.BigIntegerField(blank=True, db_column='graphicID', null=True)),
            ],
            options={
                'db_table': 'invTypes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Translationtables',
            fields=[
                ('sourcetable', models.CharField(db_column='sourceTable', max_length=200, primary_key=True)),
                ('destinationtable', models.CharField(blank=True, db_column='destinationTable', max_length=200, null=True)),
                ('translatedkey', models.CharField(db_column='translatedKey', max_length=200, primary_key=True, serialize=False)),
                ('tcgroupid', models.IntegerField(blank=True, db_column='tcGroupID', null=True)),
                ('tcid', models.IntegerField(blank=True, db_column='tcID', null=True)),
            ],
            options={
                'db_table': 'translationTables',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Trntranslationcolumns',
            fields=[
                ('tcgroupid', models.IntegerField(blank=True, db_column='tcGroupID', null=True)),
                ('tcid', models.IntegerField(db_column='tcID', primary_key=True, serialize=False)),
                ('tablename', models.CharField(db_column='tableName', max_length=256)),
                ('columnname', models.CharField(db_column='columnName', max_length=128)),
                ('masterid', models.CharField(blank=True, db_column='masterID', max_length=128, null=True)),
            ],
            options={
                'db_table': 'trnTranslationColumns',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Trntranslationlanguages',
            fields=[
                ('numericlanguageid', models.IntegerField(db_column='numericLanguageID', primary_key=True, serialize=False)),
                ('languageid', models.CharField(blank=True, db_column='languageID', max_length=50, null=True)),
                ('languagename', models.CharField(blank=True, db_column='languageName', max_length=200, null=True)),
            ],
            options={
                'db_table': 'trnTranslationLanguages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Trntranslations',
            fields=[
                ('tcid', models.IntegerField(db_column='tcID', primary_key=True, serialize=False)),
                ('keyid', models.IntegerField(db_column='keyID', primary_key=True)),
                ('languageid', models.CharField(db_column='languageID', max_length=50, primary_key=True)),
                ('text', models.TextField()),
            ],
            options={
                'db_table': 'trnTranslations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlanetSchematics',
            fields=[
                ('schematicID', models.IntegerField(db_column='schematicID', primary_key=True, serialize=False)),
                ('schematicName', models.TextField(blank=True, db_column='schematicName', null=True)),
                ('cycleTime', models.IntegerField(blank=True, db_column='cycleTime', null=True)),
            ],
            options={
                'db_table': 'planetSchematics',
            },
        ),
        migrations.CreateModel(
            name='PlanetSchematicsPinMap',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('pinType', models.ForeignKey(db_column='pinTypeID', on_delete=django.db.models.deletion.CASCADE, related_name='schematicsPinMaps', to='eve_database.InvType')),
                ('schematic', models.ForeignKey(db_column='schematicID', on_delete=django.db.models.deletion.CASCADE, related_name='schematicsPinMaps', to='eve_database.PlanetSchematics')),
            ],
            options={
                'db_table': 'planetSchematicsPinMap',
            },
        ),
        migrations.CreateModel(
            name='PlanetSchematicsTypeMap',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('isinput', models.NullBooleanField(db_column='isInput')),
                ('schematic', models.ForeignKey(db_column='schematicID', on_delete=django.db.models.deletion.CASCADE, related_name='typeMaps', to='eve_database.PlanetSchematics')),
                ('type', models.ForeignKey(db_column='typeID', on_delete=django.db.models.deletion.CASCADE, related_name='piSchematicMaps', to='eve_database.InvType')),
            ],
            options={
                'db_table': 'planetSchematicsTypeMap',
            },
        ),
        migrations.AddField(
            model_name='planetschematics',
            name='factories',
            field=models.ManyToManyField(related_name='producedSchmatics', through='eve_database.PlanetSchematicsPinMap', to='eve_database.InvType'),
        ),
        migrations.AddField(
            model_name='planetschematics',
            name='types',
            field=models.ManyToManyField(related_name='piSchematics', through='eve_database.PlanetSchematicsTypeMap', to='eve_database.InvType'),
        ),
        migrations.AlterUniqueTogether(
            name='planetschematicstypemap',
            unique_together=set([('schematic', 'type')]),
        ),
        migrations.AlterUniqueTogether(
            name='planetschematicspinmap',
            unique_together=set([('schematic', 'pinType')]),
        ),
    ]