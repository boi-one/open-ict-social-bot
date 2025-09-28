import discord
import asyncio
import random
from enum import Enum
from Communications import SendData
from UserManager import User, userManager


class MatchState(Enum):
    INIT = 0
    START = 1
    PLAYING = 2
    OVER = 3

class Match():
    id = 0
    def __init__(self, host):
        self.id += 1
        self.invitee = None
        self.state = MatchState.INIT

        if len(userManager.whitelistedUsers) < 2:
            print("too little people")
            return
        
        invitee = None
        while invitee == None or invitee == host:
            if invitee and host:
                print(f"invitee and user are the same: {invitee.name}, {host.name}")
            invitee = userManager.whitelistedUsers[random.randrange(len(userManager.whitelistedUsers))]
        
        self.host = host
        self.invitee = invitee
        print(f"invitee and user found: {self.invitee.name}, {self.host.name}")

    def EndMatch(self):
        self.state = MatchState.OVER
        self.host = None
        self.invitee = None

    async def InviteUserForMatch(self, match, expireTime = 3):
        from Messages import disableButtons
        print(f"{self.host.name} send invite to {self.invitee.name}!")
        view = discord.ui.View()
        buttonAccept = discord.ui.Button(label="accepteer invite", style=discord.ButtonStyle.blurple)
        view.add_item(buttonAccept)

        async def accept_callback(interaction):
            if(match.state != MatchState.OVER):
                match.state = MatchState.START
                disableButtons(view)
                print(f"\nhost      : {self.host.name}\ninvitee   : {self.invitee.name}\nid        : {self.id}\nmatchstate: {match.state}")
                print("accepted")
                await SendData(match)  
                await interaction.response.defer() 
            else:
                await interaction.response.send_message("Invite niet meer geldig.", ephemeral=True)

        buttonAccept.callback = accept_callback

        def expire_callback():
            disableButtons(view)
            print("disabled")
            buttonAccept.disabled = True

        await self.invitee.member.send(f"{self.host.name} wilt een spel met je spelen.", view=view)
        await asyncio.sleep(expireTime) #todo make the invite expire
        print("expired")
        expire_callback()

    def Serialize(self):
        data = {
            "id":self.id,
            "host":self.host.Serialize() if self.host else None,
            "invitee":self.invitee.Serialize() if self.invitee else None,
            "matchState":self.state.value
        }
        print("json data:", data)
        return data
    


class MatchManager:
    matches = []
    guildID = 1414895106338848811
    def Init(self, socialBot):
        self.guild = socialBot.get_guild(self.guildID)
        print(self.guild)

    def GetUsers(self):
        if not self.guild: return

        if userManager.dbExists:
            userManager.LoadUsers()
            return

        users = []
        for member in self.guild.members:
            users.append(User(member))
            print("current users GetUsers(): ", len(users), users[len(users)-1].consent)
        userManager.SaveUsers(users)

matchManager = MatchManager()
    