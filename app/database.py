import pymysql.cursors
import pymysql

connection = pymysql.connect(host='database-1.cgsryz6jvn4j.us-east-1.rds.amazonaws.com',
                             user='masteradmin',
                             password="RzyNINEwtG7EGDZpSLcj",
                             db="polls",
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def query(sql):
    if 'SELECT' in sql:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
        return result
    else:
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                connection.commit()
        finally:
            return True
