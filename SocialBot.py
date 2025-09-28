import discord
import os
import random
from dotenv import load_dotenv

from Messages import *
from UserManager import *



class SocialBot(): #wrapper class for the bot
    def __init__(self):
        load_dotenv()
        intents = discord.Intents.all()
        intents.members = True
        intents.messages = True
        self.socialBot = discord.Bot(command_prefix='!', intents=intents)

        self.socialBot.event(self.on_ready)
        self.socialBot.event(self.on_member_join)
        self.socialBot.event(self.on_member_remove)

        @self.socialBot.slash_command(name="voorkeur", description="geef aan of je gematched wilt worden met andere gebruikers om spellen mee te spelen")
        async def CallInvite(ctx: discord.ApplicationContext):
            user = userManager.FindUser(ctx.author)
            if user:
                await Invite(user)
            else:
                print("user doesn't exist")

        @self.socialBot.slash_command(name="wmatch", description="stuur een uitnodiging naar een willekeurige gebruiker in de tribe (die open staat voor matches)")
        async def RandomUserInvite(ctx: discord.ApplicationContext):
            from Matching import Match  
            sender = userManager.FindUser(ctx.author)
            newMatch = None
            if sender:
                print(f"{sender} send invite")
                newMatch = Match(sender)

                await newMatch.InviteUserForMatch(newMatch)
        
        @self.socialBot.slash_command(name="welkom", description="Introductie tot de sociale bot voor OPEN-ICT studenten.") # Is dit wel handig want dit richt meer op heel het ict server ipv alleen onze bot en spelen
        async def welkom(ctx):
            embed = discord.Embed(
                title="Welkom bij het #social kanaal van OPEN-ICT!",
                description="Deze bot is speciaal ontwikkeld om beginnende studenten te helpen elkaar beter te leren kennen. Via deze bot kun je samen met andere studenten spellen spelen, praten en connecties opbouwen. :) ",
                color=discord.Colour.blurple()
            )
            embed.add_field(name="Wat kan deze bot?", value="- Andere studenten uitnodigen om samen te spelen\n - Meldingen ontvangen als anderen willen spelen.\n - Informatie en hulp bieden via `/hulp`.\n - Je inschrijven of uitschrijven voor notificaties.\n")
            embed.add_field(name="Interesse?", value="Wil je benaderd worden als anderen spelers zoeken zoals jou? Gebruik `/voorkeur` om je keuze te wijzigen. Je hebt ook de mogelijkheid om met het commando af te melden.")
            embed.add_field(name="Waar zijn de spellen?", value="Je vindt onze spelbibliotheek op deze website:\n [Klik hier om een spel te kiezen](http://voorbeeld.nl)\n Kies een spel en gebruik de bot om anderen uit te nodigen!")
            embed.add_field(name="Hulp nodig?", value="Gebruik het commando `/hulp` om antwoorden te vinden op veelgestelde vragen of tag @assistentie_social_bot voor persoonlijke hulp.")
            embed.set_footer(text="OPEN-ICT SOCIAL BOT")
            await ctx.respond(embed=embed)


        @self.socialBot.slash_command(name="hulp", description="Vraag om persoonlijke hulp.")
        async def hulp(ctx):
                embed = discord.Embed(
                    title="Hulp & Ondersteuning",
                    description="Hieronder vind je antwoorden op veelgestelde vragen over de social bot. Heb je nog geen uitleg gezien? Gebruik dan eerst het commando `/welkom` om te begrijpen wat de bot doet.",
                    color=discord.Colour.blurple()
                )
                embed.add_field(name="Ik kan niemand vinden om mee te spelen", value="Als je in een lobby zit maar niemand kunt vinden, is het mogelijk dat er weinig actieve gebruikers zijn op dat moment. Je kunt `/uitnodigen` gebruiken om anderen te vragen mee te doen, of zelf vrienden uitnodigen!")
                embed.add_field(name="Feedback geven of bug melden.", value="Heb je iets raars ontdekt of een idee om de bot te verbeteren? Top! [Klik hier om feedback te geven of een bug te melden.](https://github.com/boi-one/open-ict-social-bot/issues/new)")
                embed.add_field(name="Hulp nodig van echt persoon?", value="Tag **@assistentie_social_bot** en geef kort aan wat er misgaat. Een moderator of ontwikkelaar helpt je meestal binnen 24 uur verder.")
                embed.set_footer(text="OPEN-ICT SOCIAL BOT")
                await ctx.respond(embed=embed)

        async def leaderboard(ctx):
        # Hier begint de embed die ervoor zorgt dat ik een wapen in mn mond stopt
            embed = discord.Embed(
                title="Top 10 social spelers van OPEN-ICT",
                description="**De meest sociale spelers tot nu toe!**",
                color=discord.Colour.blurple()
            )
            # Test field om te kijken welke beter past
            for x in userManager.whitelistedUsers:
                embed.add_field(name="", value=x.name)
            embed.add_field(name="Hoe verzamel je punten?", value="Door matches te maken en te winnen tijdens het spellen verzamel je wins!", inline=True)

            embed.set_footer(text="Leaderboard wordt bijgewerkt wanneer de tijd rijp is.")

            await ctx.respond("Hier je leaderboard vieze sweat", embed=embed)
                

        self.socialBot.run(os.getenv('TOKEN'))
        
    async def on_ready(self):
        from Matching import matchManager
        print(f"{self.socialBot.user} is aantjes banaantjes")

        matchManager.Init(self.socialBot)
        matchManager.GetUsers()
    
    async def on_member_join(self, member):
        if member.bot:
            return

        newUser = User(member) #member is the user who just joined, this is saved in a wrapper class so its easy to save certain parts in the sql
        print("haihai", newUser.name)

        userManager.allUsers.append(newUser)
        await Invite(newUser)
    
    async def on_member_remove(self, member):
        print("baibai", member.name)

        userManager.DeleteUser(user=member)

openICTBot = SocialBot()