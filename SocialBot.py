import discord
import os
from dotenv import load_dotenv

from Matching import Matching
from Messages import *
from UserManager import User

MatchManager = Matching()

class SocialBot(): #wrapper class for the bot
    socialBot = discord.Bot()

    def __init__(self):
        load_dotenv()
        intents = discord.Intents.default()
        intents.members = True
        self.socialBot = discord.Bot(command_prefix='!', intents=intents)

        self.socialBot.event(self.on_ready)
        self.socialBot.event(self.on_member_join)
        self.socialBot.event(self.on_member_leave)
    
        self.socialBot.run(os.getenv('TOKEN'))
        
    async def on_ready(self):
        print(f"{self.socialBot.user} is aantjes banaantjes")

        MatchManager.Init(self.socialBot)
        MatchManager.GetUsers(userArray=userManager.allUsers)
    
    async def on_member_join(self, member):
        newUser = User(member) #member is the user who just joined, this is saved in a wrapper class so its easy to save certain parts in the sql
        print("haihai", newUser.name)

        userManager.allUsers.append(newUser)
        await Invite(member)
    
    async def on_member_leave(self, member): #todo: fix dit het werkt NOG niet
        print("baibai", member.name)
        print("voor", userManager.allUsers.count)
        userManager.DeleteUser(member) #misschien later id gebruiken ipv naam zodat er geen fouten kunnen komen in de search
        print("na",userManager.allUsers.count)

openICTBot = SocialBot()