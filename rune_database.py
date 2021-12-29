import json
import vars, constants
import mysql.connector

rune_ids = []
all_runes = []

mydb = mysql.connector.connect(
    host="eu02-sql.pebblehost.com",
    user="customer_243379_runes",
    password=constants.sql_pass,
    database="customer_243379_runes"
)

mycursor = mydb.cursor()
print("h")


def pretty_print(dic):
    print(json.dumps(dic, indent=4, ))


async def get_runes():
    versions = vars.watcher.data_dragon.versions_for_region(vars.region)
    runes_version = versions['n']['sticker']
    # pretty_print(runes_version)
    current_runes_list = vars.watcher.data_dragon.runes_reforged(runes_version)

    for rune in vars.prim_tree:
        all_runes.append(rune)
    for rune in vars.second_tree:
        all_runes.append(rune)

    # pretty_print(all_runes)

    for g in range(0, 6, 1):
        for i in range(0, len(current_runes_list), 1):
            #pretty_print(current_runes_list)
            for j in range(0, len(current_runes_list[i]['slots']), 1):
                # pretty_print(current_runes_list[i]['slots'][j]['runes'])
                for k in range(0, len(current_runes_list[i]['slots'][j]['runes']), 1):
                    # pretty_print(current_runes_list[i]['slots'][j]['runes'][k]['name'])
                    if current_runes_list[i]['slots'][j]['runes'][k]['name'] == all_runes[g]:
                        if g <= 3:
                            prim_style = str(current_runes_list[i]['id'])
                        else:
                            second_style = str(current_runes_list[i]['id'])
                        # pretty_print(current_runes_list[i]['slots'][j]['runes'][k]['id'])
                        rune_ids.append(str(current_runes_list[i]['slots'][j]['runes'][k]['id']))
                        print(current_runes_list[i]['slots'][j]['runes'][k]['name'])


    # GET Runes into DataBase and get Primary Style and subStye Id from Rune first and seond Ziffer

    for rune_id in rune_ids:
        print(rune_id)

    print(prim_style)
    print(second_style)

    sql = "INSERT INTO rune_id (rune_id1, rune_id2, rune_id3, rune_id4, rune_id5, rune_id6, prim_style, second_style)" \
          " VALUES ('" + rune_ids[0] + "', '" + rune_ids[1] + "', '" + rune_ids[2] + "', '" + rune_ids[3] + "', '" + \
          rune_ids[4] + "', '" + rune_ids[5] + "', '" + prim_style + "', '" + second_style + "')"

    mycursor.execute(sql)
    mydb.commit()


"""
    for i in range(0, len(vars.rand_r), 1):
        for key in current_runes_list:
            if vars.rand_items[i] == current_runes_list[key]['name']:
                rune_ids.append(key)
"""
