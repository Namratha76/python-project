import connection as c 
import mysql.connector

def customerinfo():
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM customers')
        # for row in cursor:
        #     print(f'''
        #     customer Id .............. {row[0]}  
        #     First Name ...... {row[1]}   
        #     Last Name ....... {row[2]}
        #     Age.............. {row[3]}
        #     Address............{row[4]}
        #     Phone ........... {row[5]}        
        #     ''')
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)
def insertcustomerInfo(fname, lname, age, address, phone):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO customers(firstname,lastname,age,address,phone) VALUES ('{fname}', '{lname}', '{age}' , '{address}','{phone}')")
        conn.commit()
        customerinfo()
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)   
def insertproductInfo(VIN,make,model,year,color,qty,price):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO products(VIN,make,model,year,color,qty,price) VALUES ('{VIN}', '{make}', '{model}' , '{year}', '{color}, '{qty}', '{price}')")
        conn.commit()
        productinfo()
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)  

def productinfo():
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM customers')
        for row in cursor:
            print(f'''
            VIN .............. {row[0]}  
            Make ............. {row[1]}   
            model ....... .....{row[2]}
            year...............{row[3]}
            color...............{row[4]}
            quantity........... {row[5]} 
            price...............{row[6]}       
            ''')
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)
def insertuserinfo(type_of_user):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO users(type_of_user) VALUES ('{type_of_user}')")
        conn.commit()
        userinfo()
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)   
def userinfo():
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        # for row in cursor:
        #     print(f'''
        #     customer Id .............. {row[0]}  
        #     First Name ...... {row[1]}   
        #     Last Name ....... {row[2]}
        #     Age.............. {row[3]}
        #     Address............{row[4]}
        #     Phone ........... {row[5]}        
        #     ''')
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)