import discord
from UserManager import userManager

def disableButtons(view):
    for child in view.children:
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
            try:
                await interaction.message.delete()
            except Exception:
                pass
            userManager.whitelistedUsers.append(invitee)

        async def decline_callback(interaction):
            disableButtons(view)
            await interaction.response.edit_message(content="Geen probleem.\nMet /voorkeur kan je altijd je voorkeur aanpassen.", view=view)
            try:
                await interaction.message.delete()
            except Exception:
                pass

        buttonAccept.callback = accept_callback
        buttonDecline.callback = decline_callback

        await invitee.member.send("Zou je gematched willen worden met andere gebruikers?", view=view)


#TODO:
#users kunnen toestemming geven
#users kunnen hun toestemming veranderen
#users kunnen een random match starten
    #match word gemaakt en communiceert met webserver en linkje word gestuurd door de
