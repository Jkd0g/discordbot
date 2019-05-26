import discord
import random
import fileinput

token = "***************************"

client = discord.Client()

data = ["test","oppai"]


@client.event
async def on_ready():
    print("Botが起動しました。")


@client.event
async def on_message(message):
    if message.content == "おはよう！":
        if client.user != message.author:
            m = "おはよう" + message.author.name + "さん"

            await message.channel.send(m)

@client.event
async def on_message(message):
    if message.content.startswith("!random"):
        m = (random.choice(data))
        await message.channel.send(m)




client.run(token)
