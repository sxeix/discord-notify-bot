import discord
import json
import os.path
import DatabaseController
from discord.ext import commands, tasks

def fetch_token():
    with open(os.path.join('resources', 'token')) as file: 
        token = file.readline()
    return token

def construct_user_id(id):
    return "<@{x}>".format(x=id)

client = commands.Bot(command_prefix= '!')
unsavedChanges = False

@client.event
async def on_ready():
    updateBackup.start()
    print("Notify bot is active")
    DatabaseController.connect_database()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    response =  DatabaseController.fetch_server_keywords(message.guild.name)  
    
    if response == None:
        return 
    keywords = []
    toNotify = []
    for row in response:
        if row[1] in message.content.lower():
            toNotify.append(construct_user_id(row[0]))
            keywords.append(row[1])
    
    if len(keywords) > 0 and len(toNotify) > 0:        
        await message.reply(
            "'{keywords}', was mentioned {users}"
            .format(
                keywords = ", ".join(list(set(keywords))), 
                users = " ".join(toNotify)
                )
        )
        
    await client.process_commands(message)

@client.command(description="Enter a keyword or keyphrase you would like to be notifed about. Use quotations for phrases longer than one word")
async def notify(ctx, arg):
    if len(arg) > 255:
        return
    DatabaseController.insert_keyword(ctx.guild.name, ctx.author.id, arg.lower())
    await ctx.send(
        "I have stored your keyphrase, '{keyphrase}'"
        .format(
            keyphrase = arg
            )
        )
    
@tasks.loop(seconds=60)
async def updateBackup():
    print("60 second indication")

client.run(fetch_token())