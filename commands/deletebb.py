import json

import mysql

import vars, constants

def pretty_print(dic):
    print(json.dumps(dic, indent=4, ))

async def delete_all_runes_from_db(ctx):
    mydb = mysql.connector.connect(
        host="eu02-sql.pebblehost.com",
        user="customer_243379_runes",
        password=constants.sql_pass,
        database="customer_243379_runes"
    )
    mycursor = mydb.cursor()

    sql = "SELECT * FROM league_discord_map where discord_id = '" + str(ctx.author.id) + "'"
    mycursor.execute(sql)
    result = mycursor.fetchall()


    sql = "SELECT * FROM rune_id where league_id = '" + str(result[0][1]) + "'"
    mycursor.execute(sql)
    result = mycursor.fetchall()

    if len(result) > 0:
        pretty_print(result)
        sql = "DELETE FROM rune_id WHERE league_id = '" + result[0][8] + "'"
        mycursor.execute(sql)
        mydb.commit()
        await ctx.send("LAST RUNE SET FOR <@"+str(ctx.author.id)+"> was delete of the Database!")
    else:
        await ctx.send("No Rune set found for User <@"+str(ctx.author.id)+">")
    await ctx.message.delete()

