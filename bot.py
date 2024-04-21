import discord
from discord.ext import commands
import random
import os

from bot_mantik import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def mem(ctx):
    with open('M2L1\images\mem2.png','rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)



@bot.command()
async def rastgele(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'M2L1\images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
