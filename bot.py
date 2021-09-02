import discord
import os
import random
from discord.ext.commands.core import has_permissions
from discord.ext import commands

with open("Token.txt") as f:
    contents = f.read()

token = contents

description = "I am Brian's Best Boi and these are my commands: "
client = commands.Bot(command_prefix="o7", description=description)

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("________")

@client.command(description="Latency check")
async def ping(ctx):
    await ctx.send(f"pong! {round(client.latency * 1000)}ms")

@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(token)
