-- суррогатный айди для джанго

alter table "planetSchematicsTypeMap" rename to "planetSchematicsTypeMap_old";

create table "planetSchematicsTypeMap"(
	"id" SERIAL PRIMARY KEY,
	"schematicID" integer not null,
	"typeID" integer not null,
	"quantity" integer,
	"isInput" boolean
);

insert into "planetSchematicsTypeMap" ("schematicID", "typeID", "quantity", "isInput") 
	select "schematicID", "typeID", "quantity", "isInput" from "planetSchematicsTypeMap_old";
	
drop table "planetSchematicsTypeMap_old";
	
-- select * from "planetSchematicsTypeMap_old" where
	-- ("schematicID", "typeID") not in (select "schematicID", "typeID" from "planetSchematicsTypeMap");
-- select * from "planetSchematicsTypeMap" where
	-- ("schematicID", "typeID") not in (select "schematicID", "typeID" from "planetSchematicsTypeMap_old");	


	
alter table "planetSchematicsPinMap" rename to "planetSchematicsPinMap_old";

create table "planetSchematicsPinMap"(
	"id" SERIAL PRIMARY KEY,
	"schematicID" integer not null,
	"pinTypeID" integer not null
);

insert into "planetSchematicsPinMap" ("schematicID", "pinTypeID") 
	select "schematicID", "pinTypeID" from "planetSchematicsPinMap_old";
	
drop table "planetSchematicsPinMap_old";
	
-- select * from "planetSchematicsPinMap_old" where
	-- ("schematicID", "pinTypeID") not in (select "schematicID", "pinTypeID" from "planetSchematicsPinMap");
-- select * from "planetSchematicsPinMap" where
	-- ("schematicID", "pinTypeID") not in (select "schematicID", "pinTypeID" from "planetSchematicsPinMap_old");
