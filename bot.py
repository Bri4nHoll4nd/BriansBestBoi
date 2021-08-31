import discord
import random
from discord.ext.commands.core import has_permissions
from discord.ext import commands

with open("Token.txt") as f:
    contents = f.read()

token = contents

description = "Brian's best boi in python"
client = commands.Bot(command_prefix="o7", description=description)
# intents = discord.Intents.default()
# intents.members = True
# client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("________")

@client.command()
async def ping(ctx):
    await ctx.send(f"pong! {round(client.latency * 1000)}ms")

@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
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

@client.command()
async def prune(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member} was kicked from the server")

@client.command()
async def secret(ctx):
    responses = ["eats ass on a regular basis!",
                 "is dumb as fuck!"]
    await ctx.send(f"{ctx.author.mention} {random.choice(responses)}")

client.run(token)
