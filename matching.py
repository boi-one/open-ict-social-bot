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