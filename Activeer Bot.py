import discord
import os 
from dotenv import load_dotenv

load_dotenv() 
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is aantjes banaantjes")

testingservers = []

@bot.slash_command(description="Introductie bericht van het OPEN-ICT") # Is dit wel handig want dit richt meer op heel het ict server ipv alleen onze bot en spelen
async def intro(ctx):
    embed = discord.Embed(
        title="Welkom bij het #SOCIAL kanaal!",
        description="Leuk dat je er bent! Heb je interesse om te je medestudenten te kennen? De bot helpt je daarbij, je kan mij vragen om mensen voor te zoeken om samen spellen te spelen!",
        color=discord.Colour.blurple(),
    )
    embed.add_field(name="Ik wil mij inschrijven/uitschrijven", value="Heb je eventueel interesse om uitgenodigd te worden wanneer andere studenten mensen zoeken om gezellig samen te spelen en praten? Je kan daarvoor inschrijven door de command **/opt-in** te gebruiken. Om uit te schrijven kan je ook de command **/opt-out** gebruiken.")
    embed.add_field(name="Waar kan ik de spellen spelen?", value="Wij hebben een biebliotheek aan spellen voor ieder wat wils, Je kan alle spellen in ons website bekijken door hier op de link te drukken.(http://voorbeeld.nl) ")
    embed.set_footer(text="OPEN-ICT SOCIAL BOT")
    await ctx.respond(embed=embed)

@bot.slash_command(description="Laat het huidige leaderboard zien")
async def leaderboard(ctx):
    embed = discord.Embed(
        title="Leaderboard",
        description="Top 10 spelers met het meeste wins",
        color=discord.Colour.blurple(),
    )

bot.run(os.getenv('TOKEN')) # De bot werkt pas alleen met een token.

