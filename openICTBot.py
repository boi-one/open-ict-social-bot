import discord
import os
from dotenv import load_dotenv

from matching import MatchManager

class SocialBot(): #wrapper class for the bot
    socialBot = None
    allUsers = []
    whitelistedUsers = [] #the users who accept the bots request to be matched with other users

    def __init__(self):
        load_dotenv()
        intents = discord.Intents.default()
        intents.members = True
        self.socialBot = discord.Bot(command_prefix='!', intents=intents)
        socialBot.run(os.getenv('TOKEN'))
    
    @socialBot.event
    async def on_ready():
        print(f"{socialBot.user} is aantjes banaantjes")

        MatchManager.Init(socialBot)
        MatchManager.GetUsers
    
    @socialBot.event
    async def on_member_join(self, member):
        await self.allUsers.append(member)  

openICTBot = SocialBot()