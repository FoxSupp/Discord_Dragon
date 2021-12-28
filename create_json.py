import vars, json


def pretty_print(dic):
    print(json.dumps(dic, indent=4, ))


async def fill_create_json():
    versions = vars.watcher.data_dragon.versions_for_region(vars.region)
    item_version = versions['n']['item']
    current_item_list = vars.watcher.data_dragon.items(item_version)

    current_item_list = current_item_list['data']
    item_ids = []
    items = ""


    for i in range(0, len(vars.rand_items), 1):
        for key in current_item_list:
            if vars.rand_items[i] == current_item_list[key]['name']:
                item_ids.append(key)

    for id in item_ids[:-1]:
        items += '{"id" : "' + id + '", "count" : 1},'
    items += '{"id" : "' + item_ids[-1] + '", "count" : 1}'

    itemBuild = '{"title": "Bronze Bravery Build for ' + vars.rand_champ + '","associatedMaps": [],"associatedChampions": [],"blocks": [{"type": "Bronze Bravery Items from L -> R","items": [' + items + ']}]}'
    # itemBuild = json.loads(itemBuild)

    file = open("build.json", "w")
    file.write(itemBuild)
    file.close

    #pretty_print(itemBuild)
