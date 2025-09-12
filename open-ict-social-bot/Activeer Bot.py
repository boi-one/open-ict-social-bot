import discord
import os # default module
from dotenv import load_dotenv

load_dotenv() # load all the variables from the env file
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is aantjes banaantjes")

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

@bot.command()
async def gtn(ctx):
    """A Slash Command to play a Guess-the-Number game."""

    await ctx.respond('Guess a number between 1 and 10.')
    guess = await bot.wait_for('message', check=lambda message: message.author == ctx.author)

    if int(guess.content) == 5:
        await ctx.send('You guessed it!')
    else:
        await ctx.send('Nope, try again.')

bot.run(os.getenv('TOKEN')) # run the bot with the token