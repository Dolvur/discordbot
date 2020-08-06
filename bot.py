import discord
from discord.ext import commands
import random
import json

users_prefixes = {}
default_prefix = '!'

#client = discord.Client(status=discord.Status.dnd, activity=discord.Game("Booting up"))

with open('config.json') as f:
    config = json.load(f)

TOKEN = config["TOKEN"]
print("USING TOKEN_ID:", TOKEN)

async def determine_prefix(bot, msg):
    if msg.author in users_prefixes:
        return users_prefixes[msg.author]
    return default_prefix

client = commands.Bot(command_prefix=determine_prefix, description="This is a test bot",
                      status=discord.Status.dnd, activity=discord.Game("Booting up"))


@client.command()
# Changes prefix to {message}
async def prefix(ctx, str_msg):
    users_prefixes[ctx.message.author] = str_msg
    await ctx.send(f'Prefix changed to "{str_msg}" for {ctx.message.author.mention}')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def clear(ctx, amount: int = 5):
    print(type(amount))
    await ctx.channel.purge(limit=amount)


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It Is Certain', 'It Is Decidedly So', 'Without A Doubt',
                                  'Yes Definitely', 'You May Rely On It', 'As I See It', 'Yes Most Likely',
                                  'Outlook Good', 'Signs Point To Yes', 'Yes Reply Hazy',
                                  'Try Again', 'Ask Again Later', 'Better Not Tell You Now',
                                  'Cannot Predict Now', 'Concentrate And Ask Again',
                                  'Dont Bet On It', 'My Reply Is No', 'My Sources Say No',
                                  'Outlook Not So Good', 'Very Doubtful']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.event
async def on_ready():
    print("Booting up!")
    await client.change_presence(activity=discord.Streaming(name="Me and The Boys", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
    print("Ready!")
    # print(client)

client.run(TOKEN)
