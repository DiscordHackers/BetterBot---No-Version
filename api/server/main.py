import discord
import json
import sqlite3
import datetime
import random
from api.server import base


def get_lang(guild, key):
    with open(f'data/languages/{base.options(guild)[1]}.json', encoding='utf-8') as f:
        data = json.load(f)

    return data[key]


def done(guild, args):
    em = discord.Embed(colour=0x2ecc70, title=f'<:bitty_staticyes:928361336239444060> | {get_lang(guild, "EMBED_DONE")}', description=args)
    return em

def warn(guild, args):
    em = discord.Embed(colour=0xff6700, title=f'<:bitty_warning:934486383836401704> | {get_lang(guild, "EMBED_WARN")}', description=args)
    return em

def deny(guild, args):
    em = discord.Embed(colour=0xe74444, title=f'<:bitty_staticno:928361336436576366> | {get_lang(guild, "EMBED_DENY")}', description=args)
    return em

def ban(guild, args):
    em = discord.Embed(colour=0xe74444, title=f'<a:bitty_down:890196969987932170>  | {get_lang(guild, "EMBED_BAN")}', description=args)
    return em

def rule(guild, args):
    em = discord.Embed(colour=0x000000, title=f'<:bitty_rules:935193629792804935>  | {get_lang(guild, "EMBED_RULES")}', description=args)
    return em

def embed(args, c=0x922ad3):
    em = discord.Embed(colour=c, description=args)
    return em


def time():
    return datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")


def year():
    return str(datetime.datetime.now().year)


def copyright():
    if year() == "2021":
        return "© 2021 Bitty Development"
    else:
        return f"© 2021-{year()} Bitty Development"

def paginate(text: str):
    '''Simple generator that paginates text.'''
    last = 0
    pages = []
    for curr in range(0, len(text)):
        if curr % 1980 == 0:
            pages.append(text[last:curr])
            last = curr
            appd_index = curr
    if appd_index != len(text) - 1:
        pages.append(text[last:curr])
    return list(filter(lambda a: a != '', pages))


def cleanup_code(content):
    '''Automatically removes code blocks from the code.'''
    # remove ```py\n```
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])
    return content.strip('` \n')


def random_color():
    color = ('#%06x' % random.randint(8, 0xFFFFFF))
    color = int(color[1:], 16)
    color = discord.Color(value=color)
    return color