import discord
import asyncio
from UserManager import *
import random
from enum import Enum

class MatchState(Enum):
    INIT = 0,
    START = 1,
    PLAYING = 2,
    OVER = 3



class Match():
    id = 0
    def __init__(self, host):
        self.id += 1
        self.duo = []
        self.host = None
        self.invitee = None
        self.state = MatchState.INIT
        self.duo.append(host)

        if len(userManager.whitelistedUsers) < 2:
            print("too little people")
            return
        
        invitee = None
        while invitee == None or invitee == host:
            print(f"invitee and user are the same: {invitee.name}, {host.name}")
            invitee = userManager.whitelistedUsers[random.randrange(len(userManager.whitelistedUsers))]
        
        self.host = host
        self.invitee = invitee
        self.duo.append(invitee)
        print(f"invitee and user found: {self.invitee.name}, {self.host.name}")

    def EndMatch(self):
        self.state = MatchState.OVER
        self.duo.clear()
        self.host = None
        self.invitee = None

    async def InviteUserForMatch(self, match, expireTime = 3):
        print(f"{self.host.name} send invite to {self.invitee.name}!")
        view = discord.ui.View()
        buttonAccept = discord.ui.Button(label="accepteer invite", style=discord.ButtonStyle.blurple)
        view.add_item(buttonAccept)

        async def accept_callback(interaction):
            if(match.state != MatchState.OVER):
                match.state = MatchState.START
                print(f"duo size  : {len(self.duo)}\nhost      : {self.host.name}\ninvitee   : {self.invitee.name}\nid        : {self.id}\nmatchstate: {match.state}")
                print("accepted")

        buttonAccept.callback = accept_callback

        def expire_callback():
            print("disabled")
            buttonAccept.disabled = True

        await self.invitee.member.send(f"{self.host.name} wilt een spel met je spelen.", view=view)
        await asyncio.sleep(expireTime)
        #print("expired")
        #expire_callback()

class Matching:
    guildID = 1414895106338848811
    guild = None
    def Init(self, socialBot):
        self.guild = socialBot.get_guild(self.guildID)
    
    def GetUsers(self, userArray, debug = True):
        if self.guild:
            for member in self.guild.members:
                userArray.append(User(member))

                if debug:
                    print("user:", member.name)
        print("USER AMOUNT: ", len(userArray))