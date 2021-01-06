from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash import SlashContext
from discord_slash import SlashCommandOptionType
from discord_slash.utils import manage_commands
import discord
import json
import requests

client = commands.Bot(command_prefix=('!'), case_insensitive=True, intents=discord.Intents.all())

slash = SlashCommand(client, auto_register=True)


def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
        
@slash.slash(name="policy", guild_ids=[734449727914901545], options=[manage_commands.create_option("query", "A random string.", SlashCommandOptionType.STRING, True)])
async def policy(self, ctx: SlashContext, *, query):
  r = requests.get('https://api.debatev.com/api/v1/bot?q={}&dtype=hspolicy,college,openev'.format(query))
  j = json.loads(r.text)
  embed = discord.Embed(title="Results for " + query, color=0x1d68e0)
  for i in range(5):
    id = j['_source' + str(i)][0].strip('_id: ')
    tag = str(i+1) + '. ' + j['_source' + str(i)][1]['tag']
    embed.add_field(name = remove_html_tags(tag), value = "https://www.debatev.com/search/" + id, inline=False)
  embed.set_footer(text="Results given by https://debatev.com")
  await ctx.send(embed=embed)

@slash.slash(name="ld", guild_ids=[734449727914901545], options=[manage_commands.create_option("query", "A random string.", SlashCommandOptionType.STRING, True)])
async def ld(self, ctx: SlashContext, *, query):
  r = requests.get('https://api.debatev.com/api/v1/bot?q={}&dtype=ld'.format(query))
  j = json.loads(r.text)
  embed = discord.Embed(title="Results for " + query, color=0x1d68e0)
  for i in range(5):
    id = j['_source' + str(i)][0].strip('_id: ')
    tag = str(i+1) + '. ' + j['_source' + str(i)][1]['tag']
    embed.add_field(name = remove_html_tags(tag), value = "https://www.debatev.com/search/" + id, inline=False)
  embed.set_footer(text="Results given by https://debatev.com")
  await ctx.send(embed=embed)

@slash.slash(name="pf", guild_ids=[734449727914901545], options=[manage_commands.create_option("query", "A random string.", SlashCommandOptionType.STRING, True)])
async def pf(self, ctx: SlashContext, *, query):
  r = requests.get('https://api.debatev.com/api/v1/bot?q={}&dtype=pf'.format(query))
  j = json.loads(r.text)
  embed = discord.Embed(title="Results for " + query, color=0x1d68e0)
  for i in range(5):
    id = j['_source' + str(i)][0].strip('_id: ')
    tag = str(i+1) + '. ' + j['_source' + str(i)][1]['tag']
    embed.add_field(name = remove_html_tags(tag), value = "https://www.debatev.com/search/" + id, inline=False)
  embed.set_footer(text="Results given by https://debatev.com")
  await ctx.send(embed=embed)

client.run('Nzk2NDE0MzYyNzE2NzMzNDYw.X_XkrA.r4xOHzeV4Qr3x-xcEf_N12UQ2nY')