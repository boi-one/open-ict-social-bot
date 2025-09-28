import discord
from UserManager import userManager

def disableButtons(view):
    print("disable")
    for child in view.children:
        print("cji;d")
        if isinstance(child, discord.ui.Button):
            child.disabled = True

async def Invite(invitee):
        view = discord.ui.View()
        buttonAccept = discord.ui.Button(label="accepteer", style=discord.ButtonStyle.green)
        buttonDecline = discord.ui.Button(label="wijs af", style=discord.ButtonStyle.red)
        view.add_item(buttonAccept)
        view.add_item(buttonDecline)

        async def accept_callback(interaction):
            disableButtons(view)
            await interaction.response.edit_message(content="Vanaf nu zal je ge-invite kunnen worden!\nMet /voorkeur kan je altijd je voorkeur aanpassen.", view=view)
            invitee.consent = True

            if invitee in userManager.whitelistedUsers:
                 print("already whitelisted")
            else:
                userManager.whitelistedUsers.append(invitee)
                userManager.SaveUsers(userManager.allUsers)

        async def decline_callback(interaction):
            disableButtons(view)
            await interaction.response.edit_message(content="Geen probleem.\nMet /voorkeur kan je altijd je voorkeur aanpassen.", view=view)
            if invitee in userManager.whitelistedUsers:
                print("wl users ", len(userManager.whitelistedUsers))
                userManager.whitelistedUsers.remove(invitee)
                userManager.SaveUsers(userManager.allUsers)
                print("user removed ", len(userManager.whitelistedUsers))

        buttonAccept.callback = accept_callback
        buttonDecline.callback = decline_callback

        await invitee.member.send("Zou je gematched willen worden met andere gebruikers?", view=view) 

async def SendMatchLink(link, match):
       await match.host.member.send(f"klik hier om mee te doen met de match: {link}")
       await match.invitee.member.send(f"klik hier om mee te doen met de match: {link}") 

# TODO:
# fix de invite time en dat de invite kan verlopen
