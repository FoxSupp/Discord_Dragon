import json

import discord

from commands import help, summoner_rank
from commands.bronze_bravery import bronze_bravery_command
import vars
from create_json import fill_create_json
import funcs
import constants as const

vars.empty_vars()
vars.init()


def pretty_print(dic):
    print(json.dumps(dic, indent=4, ))


@vars.client.event
async def on_ready():
    await vars.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=".help "))
    print("Ready")


@vars.client.command()
async def test(ctx):
    await ctx.send('Works')


"""Bronze Bravery Command"""

@vars.client.command(name="bb")
async def cmd_bronze_bravery(ctx, pm=""):
    await bronze_bravery_command(ctx, pm)
    await ctx.message.delete()


"""Summoner Rank Command"""


@vars.client.command(name="sr")
async def cmd_summoner_rank(ctx, arg_sum="", arg_reg="euw1"):
    await summoner_rank.sr(ctx, const.api_key, arg_sum, arg_reg)


@vars.client.command(name="help")
async def cmd_help(ctx, cmd=""):
    # await help.help_command(ctx)
    await help.help_command(ctx, cmd)


vars.client.run(const.bot_id)
