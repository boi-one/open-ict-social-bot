import discord
from UserManager import userManager
userManager = userManager

async def Invite(invitee):
        buttonAccept = discord.ui.Button(label="accepteer", style=discord.ButtonStyle.green)
        buttonDecline = discord.ui.Button(label="wijs af", style=discord.ButtonStyle.red)

        async def accept_callback(interaction):
            await interaction.response.send_message("Thank you for joining!", ephemeral=True)

        async def decline_callback(interaction):
            await interaction.response.send_message("bruh", ephemeral=True)

        buttonAccept.callback = accept_callback
        buttonDecline.callback = decline_callback

        view = discord.ui.View()
        view.add_item(buttonAccept)
        view.add_item(buttonDecline)
        await invitee.send("Zou je mee willen doen aan ", view=view)
