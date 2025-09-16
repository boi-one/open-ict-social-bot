@bot.event # De bot stuurt een introductie bericht naar de beginnende student die de server aansluit
async def on_member_join(member):
    await member.send(
        f'Welkom bij OPEN-ICT van Hogeschool Utrecht, {member.mention}!
Leuk dat je er bent! Neem eerst even een kijkje bij #regels om op de hoogte te zijn van onze afspraken binnen de server. Onze bot staat klaar om je te ondersteunen, en via deze server kun je gemakkelijk communiceren met medestudenten en coaches.
Wil je je medestudenten leren kennen? Neem dan vooral een kijkje in **#SOCIAL!** Daar kun je gezellig praten, vragen stellen of gewoon even ontspannen met anderen uit de OPEN-ICT.
Let erop dat je nickname gelijk moet zijn aan je voor- en achternaam. Zo voldoe je aan onze regels, word je juist ingedeeld in groepen en ben je herkenbaar voor studenten en coaches.
Als je nickname nu goed staat, kun je dit bericht verder negeren en wensen je een fijne studie toe!
    )

