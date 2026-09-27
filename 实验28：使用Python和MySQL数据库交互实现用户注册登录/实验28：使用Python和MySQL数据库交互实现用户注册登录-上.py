# ==========第一步：创建数据库并进行数据初始化==========
#使用 pymysql 实现用户注册登录程序:教材实践任务 1
#1.首先创建数据库 pymysql 和表 users
import pymysql

#连接数据库
conn = pymysql.connect(
    host= 'localhost',
    user = 'root',
    password = '123456',
    charset = 'utf8')


#获得游标
cursor = conn.cursor()
#创建数据库
sql_create = 'create database if not exists pymysqldb'
cursor.execute(sql_create)

#创建数据表
sql_db = 'use pymysqldb'
cursor.execute(sql_db)
sql_table = 'create table if not exists users(\
id int unsigned auto_increment not null primary key,\
user_name varchar(20) not null,\
user_pwd char(40) not null,\
is_delete bit not null default 0 \
)'
cursor.execute(sql_table)

#插入数据
sql = "insert into users (user_name,user_pwd) values ('pythonuser','123456')"
cursor.execute(sql)
conn.commit()


