import discord
from discord.ext import commands

client = commands.Bot(command_prefix= '!')
servers = dict()

@client.event
async def on_ready():
    print("Notify bot is active")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.guild.id in servers:
        for user in servers[message.guild.id]:
            for keyword in servers[message.guild.id][user]:
                if keyword in message.content.lower():
                    userId ="<@{id}>".format(id=user.id)
                    await message.reply(
                        "'{keyword}', was mentioned {user}"
                        .format(
                            keyword = keyword, 
                            user = userId
                            )
                        )
                    print(user, servers[message.guild.id][user])
    await client.process_commands(message)

@client.command(description="Enter a keyword or keyphrase you would like to be notifed about use quotations for phrases longer than one word")
async def notify(ctx, arg):
    if ctx.guild.id not in servers:
        servers[ctx.guild.id] = dict()
    if ctx.author not in servers[ctx.guild.id]:
        servers[ctx.guild.id][ctx.author] =[]
    servers[ctx.guild.id][ctx.author].append(arg.lower())
    await ctx.send(
        "I have stored your keyphrase, '{keyphrase}'"
        .format(
            keyphrase = arg
            )
        )

def fetchToken():
    with open('token') as file: 
        token = file.readline()
    return token

client.run(fetchToken())