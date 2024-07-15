import discord

client = discord.Client()

bannedWords = ["rohit"]

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    msg = msg.lower()
    
    if message.content.startswith(".status"):
        await message.channel.send("Bot initialized")

    if any(word in msg for word in bannedWords):
       await message.delete()

client.run("INSERT TOKEN HERE")