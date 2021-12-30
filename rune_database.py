import json
from time import sleep

import vars, constants
import mysql.connector

all_runes = []






def pretty_print(dic):
    print(json.dumps(dic, indent=4, ))


async def get_runes(discord_id):
    mydb = mysql.connector.connect(
        host="eu02-sql.pebblehost.com",
        user="customer_243379_runes",
        password=constants.sql_pass,
        database="customer_243379_runes"
    )
    mycursor = mydb.cursor()
    versions = vars.watcher.data_dragon.versions_for_region(vars.region)
    runes_version = versions['n']['sticker']
    # pretty_print(runes_version)
    current_runes_list = vars.watcher.data_dragon.runes_reforged(runes_version)
    all_runes.clear()
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
                            vars.prim_style = str(current_runes_list[i]['id'])
                        else:
                            vars.second_style = str(current_runes_list[i]['id'])
                        # pretty_print(current_runes_list[i]['slots'][j]['runes'][k]['id'])
                        vars.rune_ids.append(str(current_runes_list[i]['slots'][j]['runes'][k]['id']))
                        #print(current_runes_list[i]['slots'][j]['runes'][k]['name'])


    # GET Runes into DataBase and get Primary Style and subStye Id from Rune first and seond Ziffer

    for rune_id in vars.rune_ids:
        #print(rune_id)
        pass
    print("----------------------")
    all_runes.clear()
    #print(prim_style)
    #print(second_style)

    sql = "SELECT * FROM league_discord_map where discord_id = '" + str(discord_id) + "'"
    mycursor.execute(sql)
    result_map = mycursor.fetchall()
    pretty_print(result_map)
    if len(result_map) > 0:

        sql = "SELECT * FROM rune_id where league_id = '" + str(result_map[0][1]) + "'"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        if(len(result) > 0):
            sql = "DELETE FROM rune_id WHERE league_id = '" + result[0][8] + "'"
            mycursor.execute(sql)
            mydb.commit()

        print("Write into database")
        sql = "INSERT INTO rune_id (rune_id1, rune_id2, rune_id3, rune_id4, rune_id5, rune_id6, prim_style, second_style, league_id)" \
          " VALUES ('" + vars.rune_ids[0] + "', '" + vars.rune_ids[1] + "', '" + vars.rune_ids[2] + "', '" + vars.rune_ids[3] + "', '" + \
          vars.rune_ids[4] + "', '" + vars.rune_ids[5] + "', '" + vars.prim_style + "', '" + vars.second_style + "', '" + result_map[0][1] + "')"
        mycursor.execute(sql)
        mydb.commit()
    vars.empty_vars()





"""
    for i in range(0, len(vars.rand_r), 1):
        for key in current_runes_list:
            if vars.rand_items[i] == current_runes_list[key]['name']:
                rune_ids.append(key)
"""
