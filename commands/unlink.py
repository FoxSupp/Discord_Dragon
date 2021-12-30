import mysql

import vars, constants


async def unlink_command(ctx):
    mydb = mysql.connector.connect(
        host="eu02-sql.pebblehost.com",
        user="customer_243379_runes",
        password=constants.sql_pass,
        database="customer_243379_runes"
    )

    mycursor = mydb.cursor()

    sql = "DELETE FROM league_discord_map WHERE discord_id = '" + str(ctx.author.id) + "'"
    mycursor.execute(sql)
    mydb.commit()