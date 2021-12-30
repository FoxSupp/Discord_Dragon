import json
from time import sleep
import asyncio

import discord

import rune_database
from commands import help, summoner_rank, link, deletebb, unlink
from commands.bronze_bravery import bronze_bravery_command
import vars
import constants as const


vars.init()


def pretty_print(dic):
    print(json.dumps(dic, indent=4, ))


@vars.client.event
async def on_ready():
    vars.empty_vars()
    await vars.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=".help "))
    print("Ready")



@vars.client.command()
async def test(ctx):
    await ctx.send('Works')


"""Bronze Bravery Command"""

@vars.client.command(name="bb")
async def cmd_bronze_bravery(ctx, pm=""):
    if vars.rand_champ == "":
        await bronze_bravery_command(ctx, pm)
        await ctx.message.delete()
        #Discord ID mit in die DB schreiben
    else:
        await ctx.send("Wait For Other Command to finish!")

@vars.client.command(name="delbb")
async def cmd_delete_bb(ctx):
    await deletebb.delete_all_runes_from_db(ctx)


"""Summoner Rank Command"""


@vars.client.command(name="sr")
async def cmd_summoner_rank(ctx, arg_sum="", arg_reg="euw1"):
    await summoner_rank.sr(ctx, const.api_key, arg_sum, arg_reg)


@vars.client.command(name="help")
async def cmd_help(ctx, cmd=""):
    await help.help_command(ctx, cmd)

@vars.client.command(name="link")
async def cmd_link(ctx, league_id=""):
    if league_id != "":
        await link.link_command(ctx, league_id)
        await ctx.message.delete()
        await ctx.author.send("Your League ID was linked to your Discord ID, you can now use the Desktop App to import your Runes")
    else:
        await ctx.message.delete()
        await ctx.send("Please provide your League ID you get from the Desktop App!")

@vars.client.command(name="unlink")
async def cmd_unlink(ctx):
    await unlink.unlink_command(ctx)
    await ctx.send("Your Discord Account has successfully been unlinked.")

vars.client.run(const.bot_id)
