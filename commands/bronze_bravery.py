import json
from random import randrange

import discord

import funcs
import rune_database
import vars
from create_json import fill_create_json


async def bronze_bravery_command(ctx, pm):
    colors = {"green": 0x00ff00, "red": 0xff0000, "blue": 0x0000ff}
    await funcs.get_everything()

    runes = "\n- ".join(vars.prim_tree) + "\n- " + "\n- ".join(vars.second_tree) + "\n\n- " + "\n- ".join(
        vars.statChips)

    embedded = discord.Embed(title='Bronze Bravery for ' + ctx.author.name, description="Bronze Bravery Build",
                             color=colors['green'])
    embedded.set_image(url=vars.splash_link)
    embedded.set_footer(text="\u3000" * 8000)
    embedded.add_field(name="Champion", value=vars.rand_champ, inline=True)
    embedded.add_field(name="Summoner Spells",
                       value=":" + "_Summoner_Spell:, :".join(vars.rand_spell) + "_Summoner_Spell:",
                       inline=False)
    embedded.add_field(name="Runes", value="- " + runes, inline=True)

    for i in vars.client.guilds:
        emoji = i.emojis
    emojis1 = vars.client.get_guild(923660327013449738).emojis
    emojis2 = vars.client.get_guild(923670142439792640).emojis
    emojis = emojis1 + emojis2
    """GET EMOJI NAME"""
    mapping = open('items.json')
    mapping = mapping.read()
    mapping = json.loads(mapping)

    emoji_item_names = []
    emoji_pics = []
    item_show = []

    for i in range(0, len(vars.rand_items), 1):
        if vars.rand_items[i] in mapping:
            emoji_item_names.append(mapping[vars.rand_items[int(i)]])
    for mapped_list in emoji_item_names:
        for emoji in emojis:
            if (mapped_list.replace(":", "") == emoji.name):
                emoji_pics.append("<:" + emoji.name + ":" + str(emoji.id) + ">")

    for i in range(0, 6, 1):
        item_show.append(emoji_pics[i] + vars.rand_items[i])

    embedded.add_field(name="Items", value="- " + "\n- ".join(item_show), inline=True)

    skill_dic = {
        0: "Q",
        1: "W",
        2: "E"
    }
    embedded.add_field(name="Max first", value=skill_dic[randrange(0, len(skill_dic), 1)], inline=False)


    channel = ctx.channel
    await fill_create_json()
    if pm=="y":

        await ctx.author.send(file=discord.File("build.json"), embed=embedded)



    await channel.send(file=discord.File("build.json"), embed=embedded)
    await rune_database.get_runes(ctx.author.id)

    vars.empty_vars()
