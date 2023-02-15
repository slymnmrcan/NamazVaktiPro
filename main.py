import datetime
import requests
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

intents = discord.Intents.all()
Bot = commands.Bot(command_prefix="/",intents=intents)
api_token = os.getenv("collect_api_token")
vakit=["%C4%B0msak","%C3%96%C4%9Fle","Ak%C5%9Fam","%C4%B0kindi","Yats%C4%B1"]


headers = {
    'content-type': "application/json",
    'authorization': api_token
    }
url = "https://api.collectapi.com/pray/single?ezan=%C4%B0kindi&data.city=konya"
def reqCollectapi():
    try:
        response = requests.get(url, headers=headers)
        data= response.json()
    except:
        print("bir sorun oluştu")
    if data['success']:
        NamazVakti = data['result'][0]['time']
        print(NamazVakti)
        #remainingTime = data['result'][0]['remainingTime']
        #saat = data['result'][0]['hour']
        #min = data['result'][0]['min']
    return NamazVakti
        
date = datetime.datetime.now()
@Bot.event
async def on_ready():
    print("çalışyor")
    await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name="Namaz"))


@Bot.command(name="kalan")
async def kalan(ctx):
    NamazVakti = reqCollectapi()
    await ctx.send(f'en yakın namaz vakti:{NamazVakti}')



@Bot.command(name="vakit")
async def time(ctx):
    await ctx.send(f'tam tarih:{date}')

@Bot.command(name="test")
async def test(ctx):
    await ctx.send("test başarılı:")

Bot.run(os.getenv("discord_api_token"))