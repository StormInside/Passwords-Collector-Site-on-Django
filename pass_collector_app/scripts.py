import mysql.connector
def connect_mysql():
    mdb=mysql.connector.connect(
        host='localhost',
        user='user',
        password='Karina-321.',
        database="user",
        charset='utf8')
    return mycursor=mdb.cursor()
