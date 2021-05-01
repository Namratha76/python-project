import os
from os import system
import sqlOps as sql

def calculateprice_black(price):
    total_price = price-(price*0.25)
    return total_price
def calculateprice_white(price):
    print('The customer gets a bonus of $400 towards down payment')
    total_price = price-400
    return total_price
    
def calculate_specialdiscount(price):
    discount = price-(price*0.25)
    return discount
def calculate_tax(price):
    tax = price+(price*0.04)
    return tax
def calculate_specialbonus(price):
    total_price = price - 500
    return total_price
def car_seller():
type=input(' Are you a buyer or seller??')
numberOfcars = int(input('How many cars do you want to add? >> '))
sql.insertuserinfo(type)
for a in range(numberOfcars):   
    car = Cars()
    print(f'----- car  # {a + 1} -------')
    vin = int(input('What is the VIN of car? >> '))
    brand = str(input('What is the make of the car? >> '))
    car.setmake(brand)
    model = str(input('What is the model of the car ? >> '))
    car.setmodel(model)
    color = str(input('What is the color of the car ? >> '))
    car.setcolor(color)
    year = str(input('What is the year of the car? >> '))
    car.setyear(year)
    price = str(input('Enter price of the car >> '))
    car.setprice(price)
    sql.insertproductInfo(vin,brand,model,year,color,numberOfcars,price)
#   list of objects
    carlist.append(car)
