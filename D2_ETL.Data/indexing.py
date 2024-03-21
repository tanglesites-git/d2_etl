from json import dumps

import json

from IndexTables import inventory_item_info_data, collectible_info_data, damage_type_info_data, equipment_slot_info_data, lore_info_data
from Settings import Dirs

file = open(Dirs.JSON / 'DestinyInventoryItemDefinition.json', 'r', encoding='utf-8')
data = json.loads(file.read())

weapon = data[str(46125926)]

file.close()

if __name__ == '__main__':
    collectible_info_dict = collectible_info_data()
    weapon_info_dict = inventory_item_info_data()
    damage_type_info_dict = damage_type_info_data()
    equipment_slot_info_dict = equipment_slot_info_data()
    lore_info_dict = lore_info_data()

    print("DestinyInventoryItemDefinition")
    print(dumps(weapon_info_dict, indent=4))
    print()
    print("-----------------------------------------------------------------------------------------------------------")
    print()
    print("DestinyCollectibleDefinition")
    print(dumps(collectible_info_dict, indent=4))
    print()
    print("-----------------------------------------------------------------------------------------------------------")
    print()
    print("DestinyDamageTypeDefinition")
    print(dumps(damage_type_info_dict, indent=4))
    print()
    print("-----------------------------------------------------------------------------------------------------------")
    print()
    print("DestinyEquipmentSlotDefinition")
    print(dumps(equipment_slot_info_dict, indent=4))
    print()
    print("-----------------------------------------------------------------------------------------------------------")
    print()
    print("DestinyLoreDefinition")
    print(dumps(lore_info_dict, indent=4))
