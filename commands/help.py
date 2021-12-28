import discord


async def help_command(ctx, cmd):
    emb_msg = discord.Embed(title='Help Menu',
                            description="Help Menu for this Bot",
                            color=0xff0000)
    if cmd == "":

        emb_msg.add_field(name="Commands\n",
                          value="***.bb***\n\n"
                                "***Parameters:***\n"
                                "**Optional** \"y\"\n"
                                "if you want your build as a Private Message\n"
                                "**Returns**\n"
                                "Returns a Random Champion + Items and Runes for you to play Bronze Bravery with\n\n"
                                "***.sr***\n\n"
                                "***Parameters:***\n"
                                "**Required:**\n"
                                "\"<Summoner Name>\"\n"
                                "**Optional:**\n"
                                "if you want another Region than euw\n"
                                "**Returns**\n"
                                "Returns all Ranks Available for the Summoner name provided")

    elif cmd == 'bb':
        emb_msg.add_field(name="Help for the Bronze Bravery Command",
                          value="***.bb***\n\n"
                                "***Parameters:***\n"
                                "**Optional** \"y\"\n"
                                "if you want your build as a Private Message\n"
                                "**Returns**\n"
                                "Returns a Random Champion + Items and Runes for you to play Bronze Bravery with\n\n"
                                "**Tips**\n"
                                "You can import the provided Json in your League Client at\n"
                                "***Collection*** --> ***Items*** --> ***Import Items Sets***\n"
                                "The just choose your build.json and Click Save\n"
                                "***Hint***\n"
                                "*If the Save Button is Gray try dragging your Last Item a bit to the Right!*"
                          )

    await ctx.send(embed=emb_msg)
