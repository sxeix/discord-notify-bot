import discord
import re
from discord.ext import commands

client = commands.Bot(command_prefix= '!')

@client.event
async def on_ready():
    print("Notify bot is active")

@client.event
async def on_message(message):
    if message.content.startswith('!notify'):
        print("command is used")
    elif "test" in message.content:
        print("contains the word test")
    
def fetchToken():
    with open('token') as file: 
        token = file.readline()
    return token


client.run(fetchToken())
