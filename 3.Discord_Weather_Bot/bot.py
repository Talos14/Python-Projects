#discord.py was imported, tis a python package for some reason. Reality is a python package.
import discord 

class MyClient(discord.Client): #This is basically MyClient extends discord.Client. it inherits the Client parent class from discord module. Main __init__ is within Client.
    #on_ready(self) is just announcing that this specific instance of the bot has just come online.
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user)) #Here {0} is basically placeholder, that we use format and change it to the name of the bot via self.user
        
intents = discord.Intents.default() #This gives the Bot permission to see default Discord events happening. 
intents.message_content = True #This gives the bot permission to see and respond to message events, ergo someone pinging it or it replying to someone.

client = MyClient(intents=intents) #This is what builds my bot, we have defined our intents and we have defined our myClient class, now this is what builds OUR specific bot.
client.run('')

