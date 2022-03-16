import discord
import traceback
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import MissingPermissions, BotMissingPermissions, CommandNotFound, BadArgument, MissingRequiredArgument
from api.server import main


class OnCommandError(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, exception):

        if isinstance(exception, MissingPermissions):
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "MISSING_PERMISSIONS")))
        elif isinstance(exception, MissingRequiredArgument):
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "MISSING_ARGS")))
        elif isinstance(exception, BadArgument):
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "MISSING_TRYARGS")))
        elif isinstance(exception, BotMissingPermissions):
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "MISSING_BOTPERMISSIONS")))
        else:
            channel = self.client.get_channel(934869199350812692)
            embed = discord.Embed(title='Ошибка Команды', color=9579219)
            embed.add_field(name='Введённая команда', value=ctx.command)
            embed.description = f"{traceback.format_exception(type(exception), exception, exception.__traceback__)}"
            embed.timestamp = datetime.utcnow()
            await channel.send(embed=embed)

def setup(client):
    client.add_cog(OnCommandError(client))