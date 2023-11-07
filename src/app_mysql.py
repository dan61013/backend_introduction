import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='db123456')

cursor = db.cursor()
# cursor.execute("CREATE DATABASE `Bboy_test`;") # 輸入SQL語法
cursor.execute('USE `Bboy_test`;')
cursor.execute('create table `Bboy_list`(\
`Name` varchar(30) NOT NULL,\
`Age` INT);\
')

cursor.close()
db.close()