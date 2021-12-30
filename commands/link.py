import discord
import mysql

import vars, constants


async def link_command(ctx, league_id):
    mydb = mysql.connector.connect(
        host="eu02-sql.pebblehost.com",
        user="customer_243379_runes",
        password=constants.sql_pass,
        database="customer_243379_runes"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO league_discord_map (league_id, discord_id)" \
          " VALUES ('" + league_id + "', '" + str(ctx.author.id) + "')"
    mycursor.execute(sql)
    mydb.commit()
