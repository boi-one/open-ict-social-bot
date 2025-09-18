import sqlite3

class User():
    #name = None
    #id = None
    #member = None
    available = True #if user is in a match

    def __init__(self, member):
        self.name = member.name
        self.id = member.id
        self.member = member

class UserManager():
    database = None
    dbCursor = None #executes sql code
    allUsers = []
    whitelistedUsers = [] #the users who accept the bots request to be matched with other users

    def __init__(self):
        self.database = sqlite3.connect('userdata.db')
        self.dbCursor = self.database.cursor()
        #self.dbCursor.execute('blah blah sql code')

    def DeleteUser(self, user):
        self.allUsers = [u for u in self.allUsers if u.id != user.id]

    def FindUser(self, user): #todo fix dat user gevonden kan worden en kijk dan verder naar de /voorkeur command, fix ook de dubbele message in DM
        print("user ", user.name)
        if len(self.allUsers) < 1:
            print("no users in list")
            return
        
        for u in self.allUsers:
            if u.id == user.id:
                print("user found")
                return u
        print("UserManager.py FindUser(self, user): could not find user")

                

#willen we direct de database gebruiken of een array met de data?
#data base direct gebruiken KAN de applicatie trager maken
#array gebruiken zou meer memory kosten

userManager = UserManager()