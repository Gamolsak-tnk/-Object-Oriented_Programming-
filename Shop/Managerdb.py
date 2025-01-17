import mysql.connector
class Managerdb:
    def __init__(self, host , user , password , database):
        self.mydb = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )