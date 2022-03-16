import discord
from discord.ext import commands
from api.server import base, main


class OnGuildJoin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
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
    client.add_cog(OnGuildJoin(client))