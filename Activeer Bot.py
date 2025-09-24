import discord
import os 
from dotenv import load_dotenv
load_dotenv() 
from UserManager import *
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is aantjes banaantjes")

testingservers = []

@bot.slash_command(description="Introductie tot de sociale bot voor OPEN-ICT studenten.") # Is dit wel handig want dit richt meer op heel het ict server ipv alleen onze bot en spelen
async def welkom(ctx):
    embed = discord.Embed(
        title="Welkom bij het #social kanaal van OPEN-ICT!",
        description="Deze bot is speciaal ontwikkeld om beginnende studenten te helpen elkaar beter te leren kennen. Via deze bot kun je samen met andere studenten spellen spelen, praten en connecties opbouwen. :) ",
        color=discord.Colour.blurple()
    )
    embed.add_field(name="Wat kan deze bot?", value="- Andere studenten uitnodigen om samen te spelen\n - Meldingen ontvangen als anderen willen spelen.\n - Informatie en hulp bieden via `/hulp`.\n - Je inschrijven of uitschrijven voor notificaties.\n")
    embed.add_field(name="Interesse?", value="Wil je benaderd worden als anderen spelers zoeken zoals jou? Gebruik `/opt-in` om je aan te melden.\n Wil je je uitschrijven? Gebruik dan `/opt-out`.")
    embed.add_field(name="Waar zijn de spellen?", value="Je vindt onze spelbibliotheek op deze website:\n [Klik hier om een spel te kiezen](http://voorbeeld.nl)\n Kies een spel en gebruik de bot om anderen uit te nodigen!")
    embed.add_field(name="Hulp nodig?", value="Gebruik het commando `/hulp` om antwoorden te vinden op veelgestelde vragen of tag @assistentie_social_bot voor persoonlijke hulp.")
    embed.set_footer(text="OPEN-ICT SOCIAL BOT")
    await ctx.respond(embed=embed)


@bot.slash_command(description="Vraag om persoonlijke hulp.")
async def hulp(ctx):
        embed = discord.Embed(
            title="Hulp & Ondersteuning",
            description="Hieronder vind je antwoorden op veelgestelde vragen over de social bot. Heb je nog geen uitleg gezien? Gebruik dan eerst het commando `/welkom` om te begrijpen wat de bot doet.",
            color=discord.Colour.blurple()
        )
        embed.add_field(name="Ik kan niemand vinden om mee te spelen", value="Als je in een lobby zit maar niemand kunt vinden, is het mogelijk dat er weinig actieve gebruikers zijn op dat moment. Je kunt `/uitnodigen` gebruiken om anderen te vragen mee te doen, of zelf vrienden uitnodigen!",q)
        embed.add_field(name="Feedback geven of bug melden.", value="Heb je iets raars ontdekt of een idee om de bot te verbeteren? Top! [Klik hier om feedback te geven of een bug te melden.](https://github.com/boi-one/open-ict-social-bot/issues/new)")
        embed.add_field(name="Hulp nodig van echt persoon?", value="Tag **@assistentie_social_bot** en geef kort aan wat er misgaat. Een moderator of ontwikkelaar helpt je meestal binnen 24 uur verder.",)
        embed.set_footer(text="OPEN-ICT SOCIAL BOT")
        await ctx.respond(embed=embed)

# mockusers
Mockusers = [("jan", 1), ("Bertha", 2), ("hans", 1000)]

@bot.slash_command(description="Laat het huidige leaderboard zien")
async def leaderboard(ctx):
    # Hier begint de embed die ervoor zorgt dat ik een wapen in mn mond stopt
        embed = discord.Embed(
            title="Top 10 social spelers van OPEN-ICT",
            description="**De meest sociale spelers tot nu toe!**",
            color=discord.Colour.blurple()
        )
        # Test field om te kijken welke beter past
        for x in Mockusers:
            embed.add_field(name="", value=x[0])
        embed.add_field(name="Hoe verzamel je punten?", value="Door matches te maken en te winnen tijdens het spellen verzamel je wins!", inline=True)

        embed.set_footer(text="Leaderboard wordt bijgewerkt wanneer de tijd rijp is.")

        await ctx.respond("Hier je leaderboard vieze sweat", embed=embed)


bot.run(os.getenv('TOKEN')) # De bot werkt pas alleen met een token.
