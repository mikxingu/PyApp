from .Database import Database

class Users(object):

    def __init__(self, userid = 0, name = "", phone = "", email = "", username = "", password = ""):
        self.info = {}
        self.userid = userid
        self.name = name
        self.phone = phone
        self.email = email
        self.username = username
        self.password = password
    
    def insertUser(self):
        database = Database()
        try:

            c = database.connection.cursor()
            c.execute("insert into users (name, phone, email, username, password) values ('" + self.name + "', '" +
            self.phone + "', '" + self.email + "', '" +
            self.username + "', '" + self.password + "' )")

            database.connection.commit()
            c.close()
            return "User successfully created!"

        except:
            return "Error while creating user."

    def updateUser(self):
        database = Database()
        try:
            c = database.connection.cursor()

            c.execute("update users set name = '" + self.name + "', phone = '" + self.phone + "', email = '" + self.email +
            "', username = '" + self.username + "', password = '" + self.password +
            "' where userid = " + self.userid + " ")

            database.connection.commit()
            c.close()

            return "User successfully updated!"
        except:
            return "Error while updating user."

    def deleteUser(self):
        database = Database()
        try: 

            c = database.connection.cursor()

            c.execute("select * from users where userid = " + userid + "  ")
            for line in c:
                self.userid = line[0]
                self.name = line[1]
                self.phone = line[2]
                self.email = line[3]
                self.username = line[4]
                self.password = line[5]

            c.close()

            return "The search returned without errors!"
        except:
            return "Error while searching for user."