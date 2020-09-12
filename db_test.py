import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='35.238.255.61',
                             user='root',
                             password='claimcart',
                             db='claims',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `*` FROM `items` WHERE `user`=%s"
        cursor.execute(sql, ('ayushdewan02@gmail.com',))
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()