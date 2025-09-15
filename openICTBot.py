import discord
import os
from dotenv import load_dotenv

from matching import Matching

MatchManager = Matching()

class SocialBot(): #wrapper class for the bot
    socialBot = discord.Bot()
    allUsers = []
    whitelistedUsers = [] #the users who accept the bots request to be matched with other users

    def __init__(self):
        load_dotenv()
        intents = discord.Intents.default()
        intents.members = True
        self.socialBot = discord.Bot(command_prefix='!', intents=intents)

        self.socialBot.event(self.on_ready)
        self.socialBot.event(self.on_member_join)
    
        self.socialBot.run(os.getenv('TOKEN'))
        
    async def on_ready(self):
        print(f"{self.socialBot.user} is aantjes banaantjes")

        MatchManager.Init(self.socialBot)
        MatchManager.GetUsers(userArray=self.allUsers)
    
    async def on_member_join(self, member):
        self.allUsers.append(member)  

openICTBot = SocialBot()