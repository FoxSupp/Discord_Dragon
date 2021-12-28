import json

import discord
import requests


async def sr(ctx, api_key, arg_sum="", arg_reg="euw1", ):
    ranks_text = []
    ranks_rank = []
    if arg_sum != "":
        """Get ID of Summoner Name"""
        r = requests.get(
            "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + arg_sum + "?api_key=" + api_key)
        json_sum_data = r.json()
        """Get Summoner Rank Data"""
        # print(json.dumps(json_sum_data, indent=4))

        if 'status' in json_sum_data:
            if json_sum_data['status']['status_code'] == 404:
                await ctx.send('<@' + str(ctx.author.id) + '> Summoner not found!')
            elif json_sum_data['status']['status_code'] == 403:
                await ctx.send('<@' + str(ctx.author.id) + '> Please Contact the Bot Hoster/Developer!')
            else:
                await ctx.send("<@" + str(ctx.author.id) + "> Unknown Error Please Contact the bot Hoster/Developer!")
        else:

            """Get Current Summoner Rank of the provided Summoner"""
            r = requests.get(
                "https://" + arg_reg + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + json_sum_data[
                    'id'] + "?api_key=" + api_key)
            json_rank_data = r.json()

            embedded = discord.Embed(title="Ranked Stats for " + arg_sum)

            for i in range(0, len(json_rank_data), 1):

                if json_rank_data[i]['queueType'] == "RANKED_TFT_PAIRS":
                    ranks_text.append("TFT Pair Rank")
                    ranks_rank.append("Rank: " + str(json_rank_data[i]['leaguePoints']))
                elif json_rank_data[i]['queueType'] == "RANKED_FLEX_SR":
                    ranks_text.append("Ranked Flex Rank")
                    ranks_rank.append(json_rank_data[i]['tier'] + " " + json_rank_data[i]['rank'])
                elif json_rank_data[i]['queueType'] == "RANKED_SOLO_5x5":
                    ranks_text.append("Solo/Due Rank: ")
                    ranks_rank.append(json_rank_data[i]['tier'] + " " + json_rank_data[i]['rank'])
            for i in range(0, len(ranks_text), 1):
                embedded.add_field(name="\n" + ranks_text[i], value="\n" + ranks_rank[i], inline=False)
            if (len(ranks_text) > 0):
                await ctx.send(embed=embedded)
            else:
                await ctx.send("Keine Ranked Daten für ***" + arg_sum + "*** vorhanden")

    else:

        await ctx.send('<@' + str(ctx.author.id) + '> You need to enter a Summoner Name.')

    await ctx.message.delete()
