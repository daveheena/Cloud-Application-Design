import mysql.connector

from mysql.connector import errorcode

def connect():
    try:
        querystring = ""
        connection = mysql.connector.connect(user='admin', password='pizza123', host='165.227.55.19', database='pizzaordermanagement')
        cursor = connection.cursor()
        cursor.execute("select * from orders")
        result = cursor.fetchall()
        print(result)
        return connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

cnx = connect()