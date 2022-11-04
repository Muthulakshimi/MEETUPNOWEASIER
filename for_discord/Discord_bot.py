import discord
from time import sleep

def for_d(DISCORD_TOKEN,msg,file):

    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        """if message.author == client.user:
            return"""
    
        #if message.content.startswith('hello'):
        await message.channel.send('Hello!')
        sleep(2)
        await message.channel.send(file=discord.File(file))

        client.close()

    client.run(DISCORD_TOKEN)
#for_d(os.getenv('DISCORD_TOKEN2'),msg='hii therer how aer usfds',file='C:/Users/grant/OneDrive/Desktop/aws_hacks/for_discord/upvote.png')