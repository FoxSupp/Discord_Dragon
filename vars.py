# global variables
import discord
from discord.ext import commands
from riotwatcher import LolWatcher
import constants as const


def empty_vars():
    global watcher
    global region
    # CHAMPIONS
    global champ_list
    global champ_range
    # ITEMS
    global non_mythic_item_list
    global mythic_item_list
    global boots_item_list
    # SPELLS
    global spell_list

    global intents

    global rand_champ
    global rand_items
    global rand_spell
    global prim_tree
    global second_tree
    global statChips
    global splash_link

    watcher = LolWatcher(const.api_key)
    region = 'euw1'
    # CHAMPIONS
    champ_list = []
    champ_range = ""
    # ITEMS
    non_mythic_item_list = []
    mythic_item_list = []
    boots_item_list = []
    # SPELLS
    spell_list = []

    intents = discord.Intents.default()
    intents.members = True

    rand_champ = ""
    rand_items = []
    rand_spell = []
    prim_tree = []
    second_tree = []
    statChips = []
    splash_link = ""


def init():
    global client
    client = commands.Bot(command_prefix='.')
    client.remove_command("help")
