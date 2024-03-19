from json import loads

from Settings import Dirs

indexing_dict = {}


def get_value(path: str, data_dict: dict):
    is_list = False
    path_list = path.split('.')
    value = None
    for item in path_list:
        if is_list:
            value = data_dict[int(item)]
            data_dict = value
            is_list = False

            if isinstance(data_dict, list):
                is_list = True
        else:
            if item in data_dict:
                value = data_dict[item]
                data_dict = value

                if isinstance(data_dict, list):
                    is_list = True
            else:
                return None
    return value


def inventory_item_info_data():
    info_data = {
        'max_name': 0,
        'max_name_len': 0,
        'max_icon': 0,
        'max_icon_len': 0,
        'max_flavor_text': 0,
        'max_flavor_text_len': 0,
        'max_screenshot': 0,
        'max_screenshot_len': 0
    }
    with open(Dirs.JSON / 'DestinyInventoryItemDefinition.json', 'r', encoding='utf-8') as file:
        json_data = loads(file.read())
        for key, value in json_data.items():
            itemType = get_value("itemType", value)

            if itemType == 3:
                name = get_value("displayProperties.name", value)
                if name is None:
                    continue
                name_length = len(name)
                if name_length > info_data['max_name_len']:
                    info_data['max_name'] = name
                    info_data['max_name_len'] = name_length

                icon = get_value("displayProperties.icon", value)
                if icon is None:
                    continue
                icon_length = len(icon)
                if icon_length > info_data['max_icon_len']:
                    info_data['max_icon'] = icon
                    info_data['max_icon_len'] = icon_length

                flavorText = get_value("flavorText", value)
                if flavorText is None:
                    continue
                flavorText_length = len(flavorText)
                if flavorText_length > info_data['max_flavor_text_len']:
                    info_data['max_flavor_text'] = flavorText
                    info_data['max_flavor_text_len'] = flavorText_length

                screenshot = get_value("screenshot", value)
                if screenshot is None:
                    continue
                screenshot_length = len(screenshot)
                if screenshot_length > info_data['max_screenshot_len']:
                    info_data['max_screenshot'] = screenshot
                    info_data['max_screenshot_len'] = screenshot_length
    return info_data


def collectible_info_data():
    info_data = {
        'max_source_string': 0,
        'max_source_string_len': 0,
    }
    with open(Dirs.JSON / 'DestinyCollectibleDefinition.json', 'r', encoding='utf-8') as file:
        json_data = loads(file.read())
        for key, value in json_data.items():
            sourceString = get_value("sourceString", value)
            if sourceString is None:
                continue
            sourceString_length = len(sourceString)
            if sourceString_length > info_data['max_source_string_len']:
                info_data['max_source_string'] = sourceString
                info_data['max_source_string_len'] = sourceString_length
    return info_data


def damage_type_info_data():
    info_data = {
        'max_name': 0,
        'max_name_len': 0,
        'max_icon': 0,
        'max_icon_len': 0,
        'max_description': 0,
        'max_description_len': 0,
    }
    with open(Dirs.JSON / 'DestinyDamageTypeDefinition.json', 'r', encoding='utf-8') as file:
        json_data = loads(file.read())
        for key, value in json_data.items():
            name = get_value("displayProperties.name", value)
            if name is None:
                continue
            name_length = len(name)
            if name_length > info_data['max_name_len']:
                info_data['max_name'] = name
                info_data['max_name_len'] = name_length

            icon = get_value("displayProperties.icon", value)
            if icon is None:
                continue
            icon_length = len(icon)
            if icon_length > info_data['max_icon_len']:
                info_data['max_icon'] = icon
                info_data['max_icon_len'] = icon_length

            description = get_value("displayProperties.description", value)
            if description is None:
                continue
            description_length = len(description)
            if description_length > info_data['max_description_len']:
                info_data['max_description'] = description
                info_data['max_description_len'] = description_length
    return info_data


def equipment_slot_info_data():
    info_data = {
        'max_name': 0,
        'max_name_len': 0,
        'max_description': 0,
        'max_description_len': 0,
    }
    with open(Dirs.JSON / "DestinyEquipmentSlotDefinition.json", 'r', encoding='utf-8') as file:
        json_data = loads(file.read())
        for key, value in json_data.items():
            name = get_value("displayProperties.name", value)
            if name is None:
                continue
            name_length = len(name)
            if name_length > info_data['max_name_len']:
                info_data['max_name'] = name
                info_data['max_name_len'] = name_length

            description = get_value("displayProperties.description", value)
            if description is None:
                continue
            description_length = len(description)
            if description_length > info_data['max_description_len']:
                info_data['max_description'] = description
                info_data['max_description_len'] = description_length
    return info_data


def lore_info_data():
    info_data = {
        'max_description': 0,
        'max_description_len': 0,
        'max_subtitle': 0,
        'max_subtitle_len': 0,
    }
    with open(Dirs.JSON / "DestinyLoreDefinition.json", "r", encoding="utf-8") as file:
        json_data = loads(file.read())
        for key, value in json_data.items():
            description = get_value("displayProperties.description", value)
            if description is None:
                continue
            description_length = len(description)
            if description_length > info_data['max_description_len']:
                info_data['max_description'] = description
                info_data['max_description_len'] = description_length

            subtitle = get_value("subtitle", value)
            if subtitle is None:
                continue
            subtitle_length = len(subtitle)
            if subtitle_length > info_data['max_subtitle_len']:
                info_data['max_subtitle'] = subtitle
                info_data['max_subtitle_len'] = subtitle_length
    return info_data


def index_dict():
    for file in Dirs.JSON.iterdir():
        with open(file, 'r', encoding="utf-8") as file_handle:
            name = file.name.split('\\')[-1].split('.')[0]
            json_data = loads(file_handle.read())

            for key, value in json_data.items():
                if key in indexing_dict:
                    indexing_dict[key].append(name)
                else:
                    indexing_dict[key] = [name]


def find_freq():
    t_total = 0
    counter = 0
    max_len = 0
    for key, value in indexing_dict.items():
        l = len(value)
        if l > 1:
            if l > max_len:
                max_len = l

            counter += 1
        t_total += l
    return counter, max_len, t_total
