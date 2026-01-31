#discord.py was imported, tis a python package for some reason. Reality is a python package.
import asyncio
import discord 
import os
import requests
import aiohttp

BOT_TOKEN = os.getenv('BOT_TOKEN')
if BOT_TOKEN is None:
    print("Error: BOT_TOKEN environment variable not set. Please check system settings.")
    exit(1)
    
    
class MyClient(discord.Client): #This is basically MyClient extends discord.Client. it inherits the Client parent class from discord module. Main __init__ is within Client.
    #on_ready(self) is just announcing that this specific instance of the bot has just come online.
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user)) #Here {0} is basically placeholder, that we use format and change it to the name of the bot via self.user
    
    async def on_message(self, message): #on_message is where we decide how our bot responds to user messages and what commands are possible.
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):  #basic hello world command to see if bot's alive or not.
            await message.channel.send('Hello World!')
        
        if message.content.startswith('$weather'): #weather command that uses OpenWeatherMap's API to fetch weather of a user given city.
            await message.channel.send('Please provide a valid City name')
            
            def check(m):  #check method included to see if the input is from the same user who triggered the bot.
                return m.author == message.author and m.channel == message.channel
            
            #Time out block included within a try condition in the event of a user not providing a city name within 30 seconds.
            try:
                city_msg = await self.wait_for('message',check=check,timeout=30)
            except asyncio.TimeoutError:
                await message.channel.send("Timeout: Please try again and reply within 30 seconds of invoking the bot.")
                return
                
            city_name = city_msg.content  #stores the user provided city name in a variable.
            
            #invokes the openweathermap api key below
            api_key = os.getenv('WEATHER_API_KEY')
            if not api_key:
                await message.channel.send("Weather API key is not set. Please ask the admin to configure it.")
                return
            
            #url format for a request to OpenWeatherMap, i jury-rigged this, dont know how it works, probably black magic.
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
            
            #used async http instead of normal http because SonarQube in VsCode couldn't stop screaming at me.
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()  #here be the main Jason, Jason is a good guy.
                        weather = data['weather'][0]['description']
                        temp = data['main']['temp']
                        humidity = data['main']['humidity']
                        wind = data['wind']['speed']
                        icon_code = data['weather'][0]['icon']
                        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png" #Fancy icon that changes depending on if its raining or not.
                        
                        #embed county below here because normal messages aren't presentable enough.
                        embed = discord.Embed(
                            title=f"Weather in {city_name}",
                            description=f"{weather.title()} | {temp}°C",
                            color=0x62c1cc
                        )
                        embed.set_thumbnail(url=icon_url)
                        embed.add_field(name="Humidity", value=f"{humidity}%", inline=True)
                        embed.add_field(name="Wind", value=f"{wind} m/s", inline=True)
                        await message.channel.send(embed=embed)
                        
                    else:
                        await message.channel.send('City not found or unable to fetch data. Please try again a bit later.') #if this appears in chat it means we cooked fr.
        
intents = discord.Intents.default() #This gives the Bot permission to see default Discord events happening. 
intents.message_content = True #This gives the bot permission to see and respond to message events, ergo someone pinging it or it replying to someone.

client = MyClient(intents=intents) #This is what builds my bot, we have defined our intents and we have defined our myClient class, now this is what builds OUR specific bot.
client.run(BOT_TOKEN)


#Praise be to the Omnissiah. Our Machine God. 
#Yes that is a WH40K reference.
