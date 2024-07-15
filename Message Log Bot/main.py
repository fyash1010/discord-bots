import discord
import pandas

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    msg = msg.lower()
    
    if message.content.startswith('.status'):
#        channel = message.channel
        await message.channel.send('Bot initialized')
'''
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("_"):
        command = message.content.split()[0].replace("_", "")
        if len(message.content.split()) > 1:
            parameters = message.content.split()[1:]

        if command == "scan":
            data = pandas.DataFrame(colums = ["content", "time", "author"])

            async for msg in message.channel.history(limit = 10):
                if msg.auther != client.user:
                    data = data.append({"content": msg.content,
                    "time": msg.created_at, "author": msg.author.name}, ignore_index = True)

                    if len(data) == limit:
                        break

            file_location = "data.csv"
            data.to_csv(file_location)
'''
client.run("INSERT TOKEN HERE")