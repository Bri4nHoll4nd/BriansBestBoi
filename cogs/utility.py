import discord
import random
from discord.ext.commands.core import has_permissions
from discord.ext import commands

class Utility(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Utility cog loaded")

    @commands.command()
    async def prune(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    @has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} was kicked from the server")

    @commands.command()
    @has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} was banned from the server")

    @commands.command()
    @has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"{user.mention} was unbanned")
                return

def setup(client):
    client.add_cog(Utility(client))
