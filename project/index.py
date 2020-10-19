import mysql.connector
from db import *
from datetime import datetime


def dispaly():
    print("------------------------------- Restaurant -----------------------------")
    print("Press 1 to Insert Data Into Restaurant Item")
    print("Press 2 to Print All Items in Restaurant")
    print("Press 3 to Update Data of Restaurant Items")
    print("Press 4 to Delete Item from Restaurant Items")
    print("Press 5 to Selling Items from Restaurant")
    print("Press 6 to View the Summary of Today's Selling")
    print("Press Any to Exits")


def input_taken():
    while(1):
        dispaly()
        print("Enter Your Choose: ")
        x = input()
        if x=='1':
            print('Enter Item Name: ')
            name = input()
            print("Enter Price: ")
            price = input()
            insert_data('klovercloud','items',name, price)
            print("Data Insert Ucessfully!")
        elif x=='2':
            myresult = item_retrive('klovercloud','items')
            print('\nID       Name        Price')
            for y in myresult:
                print(str(y[0])+"       "+str(y[1])+"       "+str(y[2]))
            print('\n')


        elif x=='3':
            print("Enter which column's value you want to change?(ex-name/price): ")
            column = input()
            print("Enter Updated Value :")
            update = input()
            print("Enter Item ID :")
            id = input()
            update_data('klovercloud','items',column, update,id)
            print("\nUpdated Successfully!\n")

        elif x =='4':
            print("Enter Item's ID, Which You Want to Delete: ")
            id = input()
            delete_data('klovercloud','items',id)
            print("Deleted Sucessfully!")

        elif x=='5':
            print("Enter Item ID: ")
            item = input()
            # print(item)
            print("What Number of Item You want to took?(ex-1/2): ")
            number = input()
            # print(number)
            result = insert_data_into_selling_table('klovercloud','selling_data',item,number)
            print("\n"+result)

        elif x=='6':
            now = datetime.now()
            date = now.strftime('%Y-%m-%d')
            result,myresult = see_todays('klovercloud','selling_data',date)
            print("\n   Item-ID     number_of_plates        total_price     Date")
            for y in result:
                 print("\t"+str(y[0])+"               "+str(y[1])+"                   "+str(y[2])+"        "+str(y[3]))
            
            print("\t\n\nTotal Sold Item:  "+str(myresult[0][0])+"     Total Earn: "+str(myresult[0][1])+"\n\n")

        else:
            exit()



if __name__ == "__main__":

    table_item_create('klovercloud','items')
    create_selling_table('klovercloud','selling_data')
    input_taken()
