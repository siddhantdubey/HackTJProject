import pymysql.cursors

#get javascript added somehow
name = "place"
description = "cool"
lat = "0"
lng = "0"

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='mapData',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = 'INSERT INTO `markers`(`name`, `description`, `lat`, `lng`) VALUES (%s, %s, %s, %s)'
        cursor.execute(sql,(name, description, lat, lng))
    connection.commit()

finally:
    connection.close()
