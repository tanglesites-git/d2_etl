from Settings import Files

import sqlite3


class ManifestResponseRepository:

    def __init__(self):
        self.conn = sqlite3.connect(Files.MANIFEST_DATA)

    def create_manifest_data_tables(self):
        sql = """
    create table if not exists manifest_data
    (
        id                                text not null,
        destiny_inventory_item_definition text not null,
        destiny_item_category_definition  text not null,
        destiny_item_tier_type_definition text not null,
        destiny_stat_definition           text not null,
        destiny_lore_definition           text not null,
        destiny_collectible_definition    text not null,
        destiny_plug_set_definition       text not null,
        destiny_damage_type_definition    text not null,
        destiny_slot_type_definition      text not null,
        date_created                     date default current_date,
        constraint pk_manifest_data_id primary key (id)
    );
        """
        cursor = self.conn.cursor()
        cursor.executescript(sql)

    def insert_into_manifest_data_tables(self, manifest_response):
        sql = """
            insert into manifest_data 
            (
            id, 
            destiny_inventory_item_definition, 
            destiny_item_category_definition, 
            destiny_item_tier_type_definition, 
            destiny_stat_definition, 
            destiny_lore_definition, 
            destiny_collectible_definition, 
            destiny_plug_set_definition, 
            destiny_damage_type_definition, 
            destiny_slot_type_definition
            ) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """
        cursor = self.conn.cursor()
        cursor.execute(sql, [manifest_response.version,
                             manifest_response.destiny_inventory_item_definition,
                             manifest_response.destiny_item_category_definition,
                             manifest_response.destiny_item_tier_type_definition,
                             manifest_response.destiny_stat_definition,
                             manifest_response.destiny_lore_definition,
                             manifest_response.destiny_collectible_definition,
                             manifest_response.destiny_plug_set_definition,
                             manifest_response.destiny_damage_type_definition,
                             manifest_response.destiny_slot_type_definition])

    def select_manifest_data(self):
        sql = """
                select 
                        id, 
                        destiny_inventory_item_definition, 
                        destiny_item_category_definition, 
                        destiny_item_tier_type_definition, 
                        destiny_stat_definition, 
                        destiny_lore_definition, 
                        destiny_collectible_definition, 
                        destiny_plug_set_definition, 
                        destiny_damage_type_definition, 
                        destiny_slot_type_definition,
                        date_created
                        from manifest_data order by id desc limit 1;
                        """
        cursor = self.conn.cursor()
        return cursor.execute(sql)

    def select_table_paths(self):
        sql = """
        select destiny_inventory_item_definition,
               destiny_item_category_definition,
               destiny_item_tier_type_definition,
               destiny_stat_definition,
               destiny_lore_definition,
               destiny_collectible_definition,
               destiny_plug_set_definition,
               destiny_damage_type_definition,
               destiny_slot_type_definition
        from manifest_data
        order by id desc
        limit 1;
        """
        cursor = self.conn.cursor()
        return [x for x in cursor.execute(sql).fetchall()[0]]