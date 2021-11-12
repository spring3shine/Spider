import pymysql


def select_table(cursor, table_name):
    cursor.execute("select * from " + table_name)
    for row in cursor:
        print(row)


if __name__ == '__main__':
    conn = pymysql.Connect(host='localhost', user='root', password='123456')
    print(conn)

    cursor = conn.cursor()

    # 查看当前所有数据库
    cursor.execute("show databases")
    all_schemas = cursor.fetchall()
    print("--show all schemas--")
    for scheme in all_schemas:
        print(scheme)
    print("------------")

    # create database
    if cursor.execute("show databases like 'xueqiu'"):
        cursor.execute("drop database xueqiu")
    cursor.execute("create database xueqiu")
    cursor.execute("use xueqiu")

    # create table
    if cursor.execute("show tables like 'people'"):
        cursor.execute("drop table xueqiu.people")
    cursor.execute("create table people(id int auto_increment ,name varchar(20), age int, primary key(id)) engine Innodb default charset=utf8mb4")

    # insert
    cursor.execute("insert into xueqiu.people (name,age) values ('li',30)")
    cursor.execute("insert into xueqiu.people (name,age) values ('wang',18)")
    cursor.execute("insert into xueqiu.people (name,age) values ('zhang',24)")

    # select
    print("--show people--")
    select_table(cursor, "people")
    print("---------")

    # update
    print("--start update--")
    cursor.execute("update xueqiu.people set age=23 where name='zhang' ")
    select_table(cursor, "people")
    print("---------")

    # delete
    print("--start delete--")
    cursor.execute("delete from xueqiu.people where name = 'wang' ")
    select_table(cursor, "people")
    print("---------")

    # important!!! 操作数据必须提交，否则无效
    conn.commit()

    cursor.close()
    conn.close()
