class ManifestResponse:

    def __init__(self, version: str, destiny_inventory_item_definition: str,
                 destiny_item_category_definition: str,
                 destiny_item_tier_type_definition: str,
                 destiny_stat_definition: str,
                 destiny_lore_definition: str,
                 destiny_collectible_definition: str,
                 destiny_plug_set_definition: str,
                 destiny_damage_type_definition: str,
                 destiny_slot_type_definition):
        self.version = version
        self.destiny_inventory_item_definition = destiny_inventory_item_definition
        self.destiny_item_category_definition = destiny_item_category_definition
        self.destiny_item_tier_type_definition = destiny_item_tier_type_definition
        self.destiny_stat_definition = destiny_stat_definition
        self.destiny_lore_definition = destiny_lore_definition
        self.destiny_collectible_definition = destiny_collectible_definition
        self.destiny_plug_set_definition = destiny_plug_set_definition
        self.destiny_damage_type_definition = destiny_damage_type_definition
        self.destiny_slot_type_definition = destiny_slot_type_definition

    @staticmethod
    def From(Manifest):
        return ManifestResponse(
            Manifest.manifest["Response"]["version"],
            Manifest.manifest["Response"]["jsonWorldComponentContentPaths"]["en"]["DestinyInventoryItemDefinition"],
            Manifest.manifest["Response"]["jsonWorldComponentContentPaths"]["en"]["DestinyItemCategoryDefinition"],
            Manifest.manifest["Response"]["jsonWorldComponentContentPaths"]["en"]["DestinyItemTierTypeDefinition"],
            Manifest.manifest["Response"]["jsonWorldComponentContentPaths"]["en"]["DestinyStatDefinition"],
            Manifest.manifest["Response"]["jsonWorldComponentContentPaths"]["en"]["DestinyLoreDefinition"],
            Manifest.manifest["Response"]["jsonWorldComponentContentPaths"]["en"]["DestinyCollectibleDefinition"],
            Manifest.manifest["Response"]["jsonWorldComponentContentPaths"]["en"]["DestinyPlugSetDefinition"],
            Manifest.manifest["Response"]["jsonWorldComponentContentPaths"]["en"]["DestinyDamageTypeDefinition"],
            Manifest.manifest["Response"]["jsonWorldComponentContentPaths"]["en"]["DestinyEquipmentSlotDefinition"]
        )
