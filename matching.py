import discord
import threading
from UserManager import *
import random

class Match():
    duo = [] #Alleen user wrapper class

    def __init__(self, host):
        self.duo.append(host)

        if len(userManager.whitelistedUsers) < 2:
            print("too little people") #TODO: laat 2 mensen gematched worden
            return
        invitee = None
        while invitee == None or invitee == host:
            print(f"invitee and user are the same: {invitee}, {host}")
            invitee = userManager.whitelistedUsers[random.randrange(len(userManager.whitelistedUsers))]
        print(f"invitee and user ready: {invitee}, {host}")
        #hierna gebeurt een error
        self.InviteUserForMatch(host, invitee)
    
    def InviteUserForMatch(sender, user, expireTime = 3):
        print(f"{sender.name} send invite to {user.name}!")
        view = discord.ui.View()
        buttonAccept = discord.ui.Button(label="accepteer invite", style=discord.ButtonStyle.blurple)
        view.add_item(buttonAccept)

        def accept_callback():
            print("accepted")           
        buttonAccept.callback = accept_callback

        def expire_callback():
            buttonAccept.disabled = True
        a = 4
        f"wins: {a}"
        user.send(f"{sender.name} wilt een spel met je spelen.", view=view)
        threading.Timer(expireTime, expire_callback).start()

class Matching:
    guildID = 1414895106338848811
    guild = None
    def Init(self, socialBot):
        self.guild = socialBot.get_guild(self.guildID)
    
    def GetUsers(self, userArray, debug = True):
        if self.guild:
            for member in self.guild.members:
                userArray.append(member)

                if debug:
                    print("user:", member.name)
        print("USER AMOUNT: ", len(userArray))