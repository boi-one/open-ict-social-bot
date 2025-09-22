import discord
import os
import random
from dotenv import load_dotenv

from Matching import *
from Messages import *
from UserManager import User

MatchManager = Matching()

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
            
            sender = userManager.FindUser(ctx.author)
            newMatch = None
            if sender:
                print(f"{sender} send invite")
                newMatch = Match(sender)

                await newMatch.InviteUserForMatch(newMatch)

        self.socialBot.run(os.getenv('TOKEN'))
        
    async def on_ready(self):
        print(f"{self.socialBot.user} is aantjes banaantjes")

        MatchManager.Init(self.socialBot)
        MatchManager.GetUsers(userArray=userManager.allUsers)
    
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