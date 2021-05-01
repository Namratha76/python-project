import mysql.connector,os
from mysql.connector import connect
from os import environ
def returnConnection():
    conn = connect(
        host = 'database-1.cp7yyt2ybpvg.us-east-2.rds.amazonaws.com',
        user = 'admin',
        password = 'password',
        database = 'mydatabase'
    )
    return conn