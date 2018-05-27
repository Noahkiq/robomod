import discord

client = discord.Client()

lastcount = [450127763551158273, 1]


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    number = 0
    send = message.channel.send
    guild = message.guild
    channel = message.channel
    user = message.author
    if channel.id == 450120389968920577:
        try:
            number = int(message.content)
        except:
            await message.delete()

        if user.id == client.user.id:
            return
        if number-1 != lastcount[1]:
            await message.delete()
            return

        #lastcount[0] = user.id
        #lastcount[1] = number
        await message.channel.send(number + 1)
        lastcount[0] = client.user.id
        lastcount[1] = number + 1



client.run(open("token.txt").read().split("\n")[0])
