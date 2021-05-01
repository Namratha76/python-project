import os
from os import system 
from car import Cars

system('cls')
carList = []
numberOfcars = int(input('How many cars do you want to buy? >> '))
#typeOfcar = input('What is the brand name of the car >> ')
print()
for a in range(numberOfcars):   
    car = Cars()
    print(f'----- car  # {a + 1} -------')
    make = str(input('What is the make of your car? >> '))
    car.setmake(make)
    model = str(input('What is the model of your car ? >> '))
    car.setmodel(model)
    color = str(input('What is the color of your car ? >> '))
    car.setcolor(color)
    year = str(input('What is the year of your car? >> '))
    car.setyear(year)
#   list of objects
    carList.append(car)
carCounter = 1
for car in carList:
    print('---------------------------')
    print(f'CAR # {carCounter}: ')
    print(f'''
        make          ........... {car.getmake()}
        model         ........... {car.getmodel()}
        color         ........... {car.getcolor()}
        year          ........... {car.getyear()}
        
        ''')
    carCounter += 1