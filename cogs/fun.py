import discord
import random
from discord.ext.commands.core import has_permissions
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun cog loaded")

    @commands.command(aliases=["8ball"])
    async def _8ball(self, ctx, *, question):
        responses = ["It is Certain.",
                     "It is decidedly so.",
                     "Without a doubt.",
                     "Yes definitely.",
                     "You may rely on it.",
                     "As I see it, yes.",
                     "Most likely.",
                     "Outlook good.",
                     "Yes.",
                     "Signs point to yes.",
                     "Reply hazy, try again.",
                     "Ask again later.",
                     "Better not tell you now.",
                     "Cannot predict now.",
                     "Concentrate and ask again.",
                     "Don't count on it.",
                     "My reply is no.",
                     "My sources say no.",
                     "Outlook not so good.",
                     "Very doubtful."]
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

    @commands.command()
    async def secret(self, ctx):
        responses = ["eats ass on a regular basis!",
                     "is dumb as fuck!"]
        await ctx.send(f"{ctx.author.mention} {random.choice(responses)}")


def setup(client):
    client.add_cog(Fun(client))
