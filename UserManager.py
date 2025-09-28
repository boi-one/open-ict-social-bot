import sqlite3
import os

class User():
    def __init__(self, member):
        self.name = member.name
        self.uid = member.id
        self.member = member
        self.consent = False
        self.available = True
        self.wins = 0
    def Serialize(self):
        data = {
            "name":self.name,
            "consent":self.consent,
            "uid":self.uid,
            "available":self.available
        }
        return data     

class UserManager():
    database = None
    dbCursor = None #executes sql code
    allUsers = []
    whitelistedUsers = [] #the users who accept the bots request to be matched with other users

    def __init__(self):
        dbPath = 'userdata.db'
        self.dbExists = os.path.exists(dbPath)
        self.database = sqlite3.connect(dbPath)
        self.dbCursor = self.database.cursor()                   #id = 0                  #name = 1           #available = 2              #consent = 3
        self.dbCursor.execute(("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, available BOOLEAN NOT NULL, consent BOOLEAN NOT NULL)"))
        self.database.commit()

    def __del__(self): #save users when application quits
        userManager.SaveUsers(self.allUsers)

    def SaveUsers(self, users):
        for user in users:
            parameters = (int(user.uid), str(user.name), bool(user.available), bool(user.consent))
            sql = "INSERT INTO users (id, name, available, consent) VALUES (?, ?, ?, ?) ON CONFLICT(id) DO UPDATE SET name=excluded.name, available=excluded.available, consent=excluded.consent"
            self.dbCursor.execute(sql, parameters)
        self.database.commit()
        print("saved user(s)")
        print("saved ", len(self.allUsers))
        print("saved whitelist ", len(self.whitelistedUsers)) #todo: if user has given consent put in whitelist (and if not work check why)

    def LoadUsers(self):
        from Matching import matchManager

        self.dbCursor.execute("SELECT id, name, available, consent FROM users")
        rows = self.dbCursor.fetchall()
        
        if len(rows) < 1:
            print("NOTHING INSIDE")
            return
        else: print("row size ", len(rows))

        print("be4loading ", len(self.allUsers))

        for row in rows:
            user = matchManager.guild.get_member(row[0])
            if user is None:
                print("USER IS NONOOOOOONE")
                continue

            newUser = User(user)
            newUser.uid = row[0] 
            newUser.name = row[1]
            newUser.available = bool(row[2])
            newUser.consent = bool(row[3])
            self.allUsers.append(newUser)
            if newUser.consent:
                self.whitelistedUsers.append(newUser)
        print("L after ", len(self.allUsers))
        print("L after wl ", len(self.whitelistedUsers))

    def DeleteUser(self, user):
        self.allUsers = [u for u in self.allUsers if u.id != user.id]

    #used to search in allUsers array
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
    
    #used to find discord.member instance for User instance
    def FindUserWithID(self, id):
        from Matching import matchManager

        print("looking for user with id ", id)
        if len(matchManager.guild.members) < 1:
            print("no users in list")
            return None
        
        for u in matchManager.guild.members:
            if u.id == id:
                print("user found ", type(u))
                return u
        print("UserManager.py FindUser(self, user): could not find user")
        return None

userManager = UserManager()