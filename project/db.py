import mysql.connector
from datetime import datetime

def create_database(db_name):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
    )
    mycursor = mydb.cursor()
    if mycursor:
        mycursor.execute("CREATE DATABASE IF NOT EXISTS "+db_name)
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database = db_name
        )
        mycursor = mydb.cursor()
    return mycursor, mydb


def table_item_create(db_name,table_name):
    mycursor, mydb = create_database(db_name)
    mycursor.execute("CREATE TABLE IF NOT EXISTS "+table_name+"(id INT AUTO_INCREMENT PRIMARY KEY, name varchar(30), price int)")
    mydb.commit()
    return True


def insert_data(db_name,table_name,value1,value2):
    mycursor,mydb= create_database(db_name)
    mycursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = '"+db_name+"' AND table_name = '"+table_name+"';")
    result = mycursor.fetchall()[0][0]
    print('result',result)
    if result==1:
       sql = ("INSERT INTO "+table_name+"(name,price) VALUES (%s, %s)")
       val = (str(value1),int(value2))
       mycursor.execute(sql,val)
       mydb.commit()
    else:
        return -1


def delete_data(db_name,table_name,id):
    mycursor,mydb= create_database(db_name)
    mycursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = '"+db_name+"' AND table_name = '"+table_name+"';")
    result = mycursor.fetchall()[0][0]
    if result==1:
        mycursor.execute("DELETE FROM "+table_name+" WHERE id="+str(id)+";")
        mydb.commit()
    else:
        return -1


def update_data(db_name,table_name,column_name,updated_value,id):
    mycursor,mydb = create_database(db_name)
    mycursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = '"+db_name+"' AND table_name = '"+table_name+"';")
    result = mycursor.fetchall()[0][0]
    if result==1:
       mycursor.execute("UPDATE "+table_name+" SET "+column_name+" = "+ updated_value+" WHERE id = "+str(id)+"")
       mydb.commit()
    else:
        return -1


def item_retrive(db_name,table_name):
    mycursor,mydb = create_database(db_name)
    mycursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = '"+db_name+"' AND table_name = '"+table_name+"';")
    result = mycursor.fetchall()[0][0]
    if result==1:
        mycursor.execute("select * from "+table_name)
        myresult = mycursor.fetchall()
        return myresult
    else:
        return -1


def create_selling_table(db_name,table_name):
    mycursor, mydb = create_database(db_name)
    mycursor.execute("CREATE TABLE IF NOT EXISTS "+table_name+"(item_id int ,FOREIGN KEY (item_id) REFERENCES Items(id) ON DELETE CASCADE, number_of_plates int, total_price int,date_time Date)")
    mydb.commit()
    return True


def insert_data_into_selling_table(db_name,table_name,item_id,numbers_of_plates):
    mycursor, mydb = create_database(db_name)
    mycursor.execute("select price from items where id = "+str(item_id))
    result = mycursor.fetchall()
    price = total_price = 0
    if not result:
        return "empty"
    else:
        price = result[0][0]
        # total_price = (int(price) * int(numbers_of_plates))

    total = (int(price) * int(numbers_of_plates))
    now = datetime.now()
    date = now.strftime('%Y-%m-%d')
    sql = ("INSERT INTO "+table_name+"(item_id,number_of_plates,total_price,date_time) VALUES (%s, %s,%s,%s)")
    val = (int(item_id),int(numbers_of_plates),int(total),str(date))
    mycursor.execute(sql,val)
    mydb.commit()
    return str(numbers_of_plates)+" item sold"


def see_todays(db_name,table_name,date):
    mycursor, mydb = create_database(db_name)
    mycursor.execute("SELECT * FROM "+table_name+" WHERE date_time='"+str(date)+"'")
    result = mycursor.fetchall()
    mycursor.execute("SELECT SUM(number_of_plates), SUM(total_price) from "+table_name+" where date_time='"+str(date)+"'")
    myresult = mycursor.fetchall()
    return result,myresult


