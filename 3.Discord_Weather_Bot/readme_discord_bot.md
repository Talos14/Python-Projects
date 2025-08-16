=================PROJECT BRIEF=================

This is a low traffic, low overhead discord Weather Bot built as the final project of the CodeDex Python Course.

It runs on discord.py and uses the OpenWeatherMap.org's API and is rated for 1000 Requests per day following which it will shut down on its own.
It uses asyncio instead of normal url get requests to ensure that in future when more processes are added to the bot, the get request alone doesn't block the entire process queue.
(That is what i think is supposed to happen, take that in whatever sense you want.)

This is a educational project and has no copyright, should you choose to copy it, be warned , i cannot be held responsible for any unknown code sorcery that might occur.

It uses Discord.embed to present the user requested information in a specified way with corresponding icons for clear skies and rainy skies.

Commands:
$hello: Responds to $hello with a greeting.
$weather: Responds to $weather by asking for a city name, then fetches and displays current weather info with icons.

Instructions to Run this on your pc:

This guide assumes you want to run the bot on a Windows desktop with no prior Python installation.

This guide assumes Windows with no prior Python installed.

### Step 1 – Install Python

1. [Download Python](https://www.python.org/downloads/)
2. Run installer → check **“Add Python to PATH”**
3. Verify:
   ```bash
   python --version
   ```

### Step 2 – Download the Bot

Save the file (e.g., `bot.py`) into a folder, e.g. `C:\DiscordWeatherBot`.

### Step 3 – Setup Virtual Environment

```bash
cd C:\DiscordWeatherBot
python -m venv venv
venv\Scripts\activate
```

### Step 4 – Install Dependencies

Create a `requirements.txt` if it doesn’t exist:

```
discord.py
aiohttp
```

Then install:

```bash
pip install -r requirements.txt
```

### Step 5 – Set Environment Variables

Replace with your actual keys:

```bash
set BOT_TOKEN="your_discord_bot_token_here"
set WEATHER_API_KEY="your_openweathermap_api_key_here"
```

### Step 6 – Run the Bot

```bash
python bot.py
```

If it works, you’ll see:

```
Logged on as YourBotName!
```

Now invite it to your Discord and try `$weather`.

---

Disclaimer: This is an educational project. No guarantees, no warranties, no tech support hotline. If it breaks, at least you learned something. ✌️
P.S: Yes, a LLM wrote the instruction bit of the readme. Rest of the code is written by me.

# #Dated - 16.08.2025

===================================================================================
