import pymysql

coon=pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1234')#连接数据库
cursor=coon.cursor() #创建游标对象

cursor.execute("create database if not exists xll")
cursor.execute("use xll")
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

row_affected = cursor.execute("create table t1(id INT ,name VARCHAR(20))")

row_affected1=cursor.execute("INSERT INTO t1(id,name) values (1,'alvin'),(2,'xialv')")

cursor.execute("update t1 set name = 'silv2' where id=2")


coon.commit()
cursor.close()
coon.close()










