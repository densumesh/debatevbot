from discord.ext import commands
import discord
import json
import requests

client = discord.Client()
client = commands.Bot(command_prefix=('!'), case_insensitive=True)
client.remove_command("help")

def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


class debatevbot(commands.Cog):
    @commands.command()
    async def policy(self, ctx, *, query):
      try:
        r = requests.get('https://api.debatev.com/api/v1/bot?q={}&dtype=hspolicy,college,openev'.format(query))
        j = json.loads(r.text)
        embed = discord.Embed(title="Results for " + query, color=0x1d68e0)
        for i in range(5):
          id = j['_source' + str(i)][0].strip('_id: ')
          tag = str(i+1) + '. ' + j['_source' + str(i)][1]['tag']
          embed.add_field(name = remove_html_tags(tag), value = "https://www.debatev.com/search/" + id, inline=False)
        embed.set_footer(text="Results given by https://www.debatev.com")
        await ctx.send(embed=embed)
      except KeyError:
        await ctx.send('No results found')
    
    @commands.command()
    async def ld(self, ctx, *, query):
      try:
        r = requests.get('https://api.debatev.com/api/v1/bot?q={}&dtype=ld'.format(query))
        j = json.loads(r.text)
        embed = discord.Embed(title="Results for " + query, color=0x1d68e0)
        for i in range(5):
          id = j['_source' + str(i)][0].strip('_id: ')
          tag = str(i+1) + '. ' + j['_source' + str(i)][1]['tag']
          embed.add_field(name = remove_html_tags(tag), value = "https://www.debatev.com/search/" + id, inline=False)
        embed.set_footer(text="Results given by https://debatev.com")
        await ctx.send(embed=embed)
      except KeyError:
        await ctx.send('No results found')
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Debatev Bot help", description="Some useful commands", color=ctx.message.author.color.value)
        embed.add_field(name="!policy [query]",
                        value="Searches debatev for policy cards",
                        inline=False)
        embed.add_field(name="!ld [query]",
                        value="Searches debatev for ld cards",
                        inline=False)
        embed.set_footer(text="Source: " + 'https://github.com/densumesh/my-stummy-bot')
        await ctx.send(content=None, embed=embed)



client.add_cog(debatevbot(client))
client.run('Nzk2NDE0MzYyNzE2NzMzNDYw.X_XkrA.r4xOHzeV4Qr3x-xcEf_N12UQ2nY')
