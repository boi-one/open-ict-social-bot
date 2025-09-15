import discord
import os
from dotenv import load_dotenv

from matching import MatchManager

load_dotenv() # load all the variables from the env file

intents = discord.Intents.default()
intents.members = True

socialBot = discord.Bot(command_prefix='!', intents=intents)

@socialBot.event
async def on_ready():
    print(f"{socialBot.user} is aantjes banaantjes")

    MatchManager.Init(socialBot)
    MatchManager.GetUsers
    
    

@socialBot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

@socialBot.command()
async def gtn(ctx):
    """A Slash Command to play a Guess-the-Number game."""

    await ctx.respond('Guess a number between 1 and 10.')
    guess = await bot.wait_for('message', check=lambda message: message.author == ctx.author)

    if int(guess.content) == 5:
        await ctx.send('You guessed it!')
    else:
        await ctx.send('Nope, try again.')

socialBot.run(os.getenv('TOKEN')) # run the bot with the token