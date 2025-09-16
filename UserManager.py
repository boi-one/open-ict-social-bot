import sqlite3

class User():
    name = None
    member = None

    def __init__(self, member):
        self.name = member.name

class UserManager():
    database = None
    dbCursor = None #executes sql code
    allUsers = []
    whitelistedUsers = [] #the users who accept the bots request to be matched with other users

    def __init__(self):
        self.database = sqlite3.connect('userdata.db')
        self.dbCursor = self.database.cursor()
        #self.dbCursor.execute('blah blah sql code')

    @staticmethod
    def DeleteUser(self, user):
        for u in self.allUsers:
            if u.name == user.name:
                self.allUsers.remove(u)
                return
        print("no user found")
                

#willen we direct de database gebruiken of een array met de data?
#data base direct gebruiken KAN de applicatie trager maken
#array gebruiken zou meer memory kosten

userManager = UserManager()