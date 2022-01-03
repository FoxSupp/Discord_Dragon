import json
from random import randrange
from urllib.request import urlopen

import vars

def pretty_print(dic):
    print(json.dumps(dic, indent=4, ))

async def get_everything(map="11"):


    if map.lower() == "aram":
        map = "12"
    else:
        map = "11"
    """Get all Champions and put them in a List
        then take a Random Champion out of there"""

    # Get Current Champions
    versions = vars.watcher.data_dragon.versions_for_region(vars.region)
    champions_version = versions['n']['champion']
    current_champ_list = vars.watcher.data_dragon.champions(champions_version)

    # Put all Champions in a list

    for champ in current_champ_list['data']:
        vars.champ_list.append(champ)

    # Save to Variable
    vars.rand_champ = vars.champ_list[randrange(0, len(vars.champ_list), 1)]
    temp_champ = current_champ_list['data'].get(vars.rand_champ)
    champ_range = temp_champ['stats']['attackrange']

    champ_json = urlopen(
        "http://ddragon.leagueoflegends.com/cdn/11.24.1/data/en_US/champion/" + vars.rand_champ + ".json")
    champ_json = json.loads(champ_json.read())

    rand_skin = \
    champ_json['data'][vars.rand_champ]['skins'][randrange(0, len(champ_json['data'][vars.rand_champ]['skins']), 1)][
        'num']

    vars.splash_link = "http://ddragon.leagueoflegends.com/cdn/img/champion/splash/" + vars.rand_champ + "_" + str(
        rand_skin) + ".jpg"

    """Get all Items and get 6 Random Items"""

    item_version = versions['n']['item']
    current_item_list = vars.watcher.data_dragon.items(item_version)

    pretty_print(current_item_list)

    """Boots"""
    for key in current_item_list['data']:
        if not 'into' in current_item_list['data'][key] and \
                'from' in current_item_list['data'][key] and \
                "Boots" in current_item_list['data'][key]['tags']:
            vars.boots_item_list.append(current_item_list['data'][key]['name'])

    """Non Mythic"""
    for key in current_item_list['data']:
        if not 'into' in current_item_list['data'][key] and \
                'from' in current_item_list['data'][key] and \
                len(current_item_list['data'][key]['description'].split('Mythic')) == 1 and \
                "Boots" not in current_item_list['data'][key]['tags'] and \
                current_item_list['data'][key]['maps'][map] == True and \
                "Consumable" not in current_item_list['data'][key]['tags']:
            vars.non_mythic_item_list.append(current_item_list['data'][key]['name'])

    """Mythic Items"""
    for key in current_item_list['data']:
        if len(current_item_list['data'][key]['description'].split('Mythic')) > 1:
            vars.mythic_item_list.append(current_item_list['data'][key]['name'])

    """Mythic Items hinzufügen"""
    vars.rand_items.append(vars.mythic_item_list[randrange(0, len(vars.mythic_item_list), 1)])

    """Unique Lifeline Items entfernen"""
    if (vars.rand_items[0] == "Immortal Shieldbow"):
        vars.non_mythic_item_list.remove("Sterak's Gage")
        vars.non_mythic_item_list.remove("Maw of Malmortius")
    """Boots hinzufügen"""
    vars.rand_items.append(vars.boots_item_list[randrange(0, len(vars.boots_item_list), 1)])
    """Non Mythic items hinzufügen"""
    if (champ_range < 300):
        vars.non_mythic_item_list.remove("Runaan's Hurricane")
    for i in range(0, 4, 1):
        vars.rand_items.append(vars.non_mythic_item_list[randrange(0, len(vars.non_mythic_item_list), 1)])
        """Unique Items Entfernen"""
        if (vars.rand_items[i + 2] == "Archangel's Staff" or \
                vars.rand_items[i + 2] == "Winter's Approach" or \
                vars.rand_items[i + 2] == "Manamune"):
            vars.non_mythic_item_list.remove("Archangel's Staff")
            vars.non_mythic_item_list.remove("Winter's Approach")
            vars.non_mythic_item_list.remove("Manamune")
        elif (vars.rand_items[i + 2] == "Guinsoo's Rageblade" or \
              vars.rand_items[i + 2] == "Infinity Edge"):
            vars.non_mythic_item_list.remove("Guinsoo's Rageblade")
            vars.non_mythic_item_list.remove("Infinity Edge")
        elif (vars.rand_items[i + 2] == "Maw of Malmortius" or \
              vars.rand_items[i + 2] == "Sterak's Gage"):
            vars.non_mythic_item_list.remove("Maw of Malmortius")
            vars.non_mythic_item_list.remove("Sterak's Gage")
        elif (vars.rand_items[i + 2] == "Serylda's Grudge" or \
              vars.rand_items[i + 2] == "Lord Dominik's Regards"):
            vars.non_mythic_item_list.remove("Serylda's Grudge")
            vars.non_mythic_item_list.remove("Lord Dominik's Regards")
        elif (vars.rand_items[i + 2] == "Ravenous Hydra" or \
              vars.rand_items[i + 2] == "Titanic Hydra"):
            vars.non_mythic_item_list.remove("Ravenous Hydra")
            vars.non_mythic_item_list.remove("Titanic Hydra")
        elif (vars.rand_items[i + 2] == "Silvermere Dawn" or \
              vars.rand_items[i + 2] == "Mercurial Scimitar"):
            vars.non_mythic_item_list.remove("Silvermere Dawn")
            vars.non_mythic_item_list.remove("Mercurial Scimitar")
        else:
            vars.non_mythic_item_list.remove(vars.rand_items[i + 2])

    """Get all Summoner Spells and choose 2 at Random"""

    versions = vars.watcher.data_dragon.versions_for_region(vars.region)
    summoner_spell_version = versions['n']['summoner']
    current_spell_list = vars.watcher.data_dragon.summoner_spells(summoner_spell_version)

    for spell in current_spell_list['data']:
        if current_spell_list['data'][spell]['name'] != "Smite":
            for mode in current_spell_list['data'][spell]['modes']:
                if mode == "CLASSIC":
                    vars.spell_list.append(current_spell_list['data'][spell]['name'])

    for i in range(0, 2, 1):
        vars.rand_spell.append(vars.spell_list[randrange(0, len(vars.spell_list), 1)])
        vars.spell_list.remove(vars.rand_spell[i])

    """Get all Runes and Choose a Random Combination"""

    versions = vars.watcher.data_dragon.versions_for_region(vars.region)
    runes_version = versions['n']['sticker']
    current_runes_list = vars.watcher.data_dragon.runes_reforged(runes_version)
    prim_tree_counter = randrange(0, 5, 1)
    second_tree_counter = randrange(0, 5, 1)
    while second_tree_counter == prim_tree_counter:
        second_tree_counter = randrange(0, 5, 1)

    line_counter_1 = 0
    line_counter_2 = 10
    column_counter = 0

    random_tree = current_runes_list[prim_tree_counter]['slots']

    """Get the Primary Tree Runes"""
    for line_counter_1 in range(0, 4, 1):
        vars.prim_tree.append(
            random_tree[line_counter_1]['runes'][randrange(0, len(
                random_tree[line_counter_1]['runes']), 1)]['name'])

    """Get the Secondary Tree"""
    random_tree = current_runes_list[second_tree_counter]['slots']
    for i in range(0, 2, 1):

        line_counter_1 = randrange(1, 4, 1)
        while line_counter_2 == line_counter_1:
            line_counter_1 = randrange(1, 4, 1)
        line_counter_2 = line_counter_1

        vars.second_tree.append(
            random_tree[line_counter_1]['runes'][randrange(0, len(
                random_tree[line_counter_1]['runes']), 1)]['name'])

    """Get Random StatStips"""
    statChipsArray = [["Adaptive", "AttackSpeed", "Cooldown"], ["Adaptive", "Armor", "Magic Resist"],
                      ["Health", "Armor", "Magic Resist"]]

    for i in range(0, 3, 1):
        vars.statChips.append(statChipsArray[i][randrange(0, 3, 1)])
