import mysql.connector
from mysql.connector import Error

class database:
    connection = None
    messages = []
    def __init__(self, host_name, user_name, user_password, db_name):

        try:
            database.connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
            print("Connection to MySQL DB successful")
            database.messages.append("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")
            database.messages.append(f"The error '{e}' occurred")

    def execute(self, query):
        cursor = database.connection.cursor(buffered=True)
        try:
            cursor.execute(query)
            result = cursor.fetchone()
            database.connection.commit()
            print("Executed '" + query + "'")
            database.messages.append("Executed '" + query + "'")
            print(result)
            database.messages.append(result)
        except Error as e:
            print(f"The error '{e}' occurred")
            database.messages.append(f"The error '{e}' occurred")



