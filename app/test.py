import discord
from discord.ext import commands
import time
import requests
import psutil
from app.utility import second_parser
from app.utility import Database_connection_check

BOT_TOKEN = "MTAxMzg5ODAxMzE3OTEyNTg4MQ.GwgYuz.xCMVAYWITU9YLhOcmtFObL67MQTgaCT1iw8kKE"
BOT_PREFIX = "!"
intents = discord.Intents.default()
client = commands.Bot(command_prefix=BOT_PREFIX, help_command=None, intents=intents)


@client.event
async def on_ready():
    print('Bot Online!')

@client.command()
async def status(ctx):

    # Latency measurement
    url = "https://discord.com"
    get_uptime = requests.get(url).elapsed.total_seconds()

    # Uptime since running pc
    uptime = time.time() - psutil.boot_time()

    await ctx.send\
        (f"Uptime: {second_parser.parse_duration(uptime)}\n"
        f"Latency is: {int(get_uptime * 1000)}ms \n"
        f"Available Memory: {psutil.virtual_memory()[1] // 1000000}MB\n"
        f"Database connection: {Database_connection_check}"
         )

client.run(BOT_TOKEN)