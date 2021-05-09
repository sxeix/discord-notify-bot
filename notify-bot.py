import discord
from discord.ext import commands

client = commands.Bot(command_prefix= '!')
keywords = dict()

@client.event
async def on_ready():
    print("Notify bot is active")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    for user in keywords:
        for keyword in keywords[user]:
            if keyword in message.content:
                userId ="<@{id}>".format(id=user.id)
                await message.reply(
                    "'{keyword}', was mentioned {user}"
                    .format(
                        keyword = keyword, 
                        user = userId
                        )
                    )
                print(user, keywords[user])
    await client.process_commands(message)

@client.command(description="Enter a keyword or keyphrase you would like to be notifed about")
async def notify(ctx, arg):
    if ctx.author not in keywords:
        keywords[ctx.author] =[]
    keywords[ctx.author].append(arg)
    print(keywords)
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