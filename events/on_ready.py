import discord
import random
from discord.ext import commands, tasks
from api.server import base, main


class OnReady(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = f"swe.betterbot.ru"))
        print("ptero start")

        for guild in self.client.guilds:
            print(guild.id , guild.name)
            
            for member in guild.members:
                if not member.bot:
                    try:
                        if base.user(member) is None:
                            base.send(f"INSERT INTO users VALUES ('{member.id}', '{member.name}', 0, 0, 0)")
                        else:
                            pass
                    except:
                        continue

def setup(client):
    client.add_cog(OnReady(client))