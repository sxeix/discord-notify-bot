import discord
import json
import os.path
from discord.ext import commands, tasks

def loadServers():
    s = dict()
    if os.path.isfile("notify.json"):
        with open("notify.json", 'r') as f:
            s = json.load(f)
    return s

def fetchToken():
    with open('token') as file: 
        token = file.readline()
    return token

client = commands.Bot(command_prefix= '!')
servers = loadServers()
unsavedChanges = False

@client.event
async def on_ready():
    updateBackup.start()
    print(servers)
    print("Notify bot is active")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.guild.name in servers:
        for user in servers[message.guild.name]:
            for keyword in servers[message.guild.name][user]:
                if keyword in message.content.lower():
                    userId ="<@{id}>".format(id=user)
                    await message.reply(
                        "'{keyword}', was mentioned {user}"
                        .format(
                            keyword = keyword, 
                            user = userId
                            )
                        )
    await client.process_commands(message)

@client.command(description="Enter a keyword or keyphrase you would like to be notifed about use quotations for phrases longer than one word")
async def notify(ctx, arg):
    if ctx.guild.name not in servers:
        servers[ctx.guild.name] = dict()
    if ctx.author.id not in servers[ctx.guild.name]:
        servers[ctx.guild.name][ctx.author.id] =[]
    servers[ctx.guild.name][ctx.author.id].append(arg.lower())
    await ctx.send(
        "I have stored your keyphrase, '{keyphrase}'"
        .format(
            keyphrase = arg
            )
        )
    global unsavedChanges
    unsavedChanges = True
    
@tasks.loop(seconds=10)
async def updateBackup():
    global unsavedChanges
    print(unsavedChanges)
    if unsavedChanges:
        with open("notify.json", 'w') as f:
            json.dump(servers, f, indent=4)
        print("Changes saved")
        unsavedChanges = False

client.run(fetchToken())