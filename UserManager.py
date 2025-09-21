import sqlite3

class User():
    def __init__(self, member):
        self.name = member.name
        self.consent = False
        self.uid = member.id
        self.member = member
        self.available = True

    def Serialize(self):
        data = {
            "name":self.name,
            "consent":self.consent,
            "uid":self.uid,
            "available":self.available
        }
        return data

    def LoadUser():
        pass

class UserManager():
    database = None
    dbCursor = None #executes sql code
    allUsers = []
    whitelistedUsers = [] #the users who accept the bots request to be matched with other users

    def __init__(self):
        self.database = sqlite3.connect('userdata.db')
        self.dbCursor = self.database.cursor()
        self.dbCursor.execute(("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, available INTEGER NOT NULL CHECK (available IN (0,1)))"))
        self.database.commit()

    def SaveUsers():
        pass

    def LoadUser():
        pass

    def DeleteUser(self, user):
        self.allUsers = [u for u in self.allUsers if u.id != user.id]

    def FindUser(self, user): #supposed to return the user wrapper class and NOT a discord.member instance
        print("looking for user ", user.name)
        if len(self.allUsers) < 1:
            print("no users in list")
            return None
        
        for u in self.allUsers:
            if u.uid == user.id:
                print("user found ", type(u))
                return u
        print("UserManager.py FindUser(self, user): could not find user")
        return None

userManager = UserManager()