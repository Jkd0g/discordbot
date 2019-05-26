import discord
import random
import fileinput

token = "NTgyMDE4NjQ0MDU0Mzc2NDYw.XOnu3Q.ievlqxpJ36QR088WKRNNRz_2g34"

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
