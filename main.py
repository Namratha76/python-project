import os,datetime
import functions as func
from os import system
import sqlOps as sql
from car import Cars
from datetime import *
system('cls')

carlist=[ ]
car_make = ['toyota', 'Nissan', 'BMW', 'Audi', 'Honda']
car1=(('camry','2019','black',27000),('seqouia','2020','silver',28000),('camry','2021','white',25000))
car2= (('maxima','2019','black',22000),('maxima','2020','red',28000),('pathfinder','2021','white',26000))
car3=(('M6','2019','black',32000),('325I','2020','white',31000))
car4=(('R8','2019','black',46000),('R8','2020','white',43000))
car5=(('pilot','2019','black',21000),('civic','2020','silver',28000),('Accord','2021','white',25000))

print('-----Welcome to Car Showroom-----')
customer =int(input('please select option : 1.To create an account   2. To Authenticate '))
if (customer == 1):
    fname = input('What is your firstname? >> ')
    lname = input('What is your lastname? >> ')
    age = input('What is your age? >> ')
    address = input('What is your address? >> ')
    phone = input('What is your phone no? >> ')
    sql.insertcustomerInfo(fname, lname, age,address,phone)
elif(customer == 2):
    username = 'Namratha'
    password = 'pass'
    path = './project/logs.txt'

    user = input('What is your username? >> ')
    passwd = input('What is your password? >> ')

    def printSuccessOrNot(message):
        if (message == 'Success'):
            with open(path, 'a') as log:
                log.write(f'\nUser {user} tried to log in on {datetime.now()} - Result: {message}')
                log.close()
        else:
            with open(path, 'a') as log:
                log.write(f'\nUser {user} tried to log in on {datetime.now()} - Result: {message}')
                log.close()

    if(user == username and passwd == password):
        print(f'Hello {user}, you are fully authenticated')
        printSuccessOrNot('Success')
    else:
        print('The combination of the username and password you used does not match our records')
        printSuccessOrNot('Failed')
        exit()
else:
    print('Invalid option')
    exit()
counter = 1
for index in range(len(car_make)):
    print(f'{counter}. {car_make[index]}')
    counter += 1
option = int(input('These are the cars available for purchase -----select your option-----'))
if(option == 1):
    for car in car1:
        print(f'{car}')
elif(option == 2):
    for car in car2:
        print(f'{car}')
elif(option == 3):
    for car in car3:
        print(f'{car}')
elif(option == 4):
    for car in car4:
        print(f'{car}')
elif(option == 5):
    for car in car5:
        print(f'{car}')
else:
    print('Invalid option')
type=input(' Are you a buyer or seller??')
numberOfcars = int(input('How many cars do you want to buy? >> '))
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
path = './project/order.txt'

with open (path, 'w') as file:
    file.write('---------order summary---------')
    file.close()


# while True:
#     content = input('What content do you want to add to the file? >> ')
    
#     response = input('Do you want to add more content [Y/N]? >> ')
#     if(str.upper(response) == 'N'):
#         break
carCounter = 1
for car in carlist:
    print('--------The car you just selected  is ----------')
    print(f'CAR # {carCounter}: ')
    print(f'''
        make          ........... {car.getmake()}
        model         ........... {car.getmodel()}
        color         ........... {car.getcolor()}
        year          ........... {car.getyear()}
        price          ...........{car.getprice()}
        ''')
    carCounter += 1
print('----------Customer Details-----------')
print()

if( color =='black' and brand == 'toyota'):
    total_price = func.calculateprice_black(27000)
    tax = func.calculate_tax(total_price)
    print('---------Order summary-------')
    with open(path, 'a') as file:
        file.write(f'\nMSRP of the car : 27000\n')
        file.write(f'Total price with 25% discout = ${total_price}\n')
        file.write(f'Subtotal with(4%) tax ={tax}\n')
        file.close()
    print('MSRP of the car : 27000')
    print(f'Total price with 25% discount : ${total_price}')
    print(f'Subtotal(4%) tax : ${tax}')
elif( color == 'white' and brand == 'toyota'):
    total_price = func.calculateprice_white(25000)
    tax = func.calculate_tax(total_price)
    print('---------Order summary-------')
    with open(path, 'a') as file:
        file.write(f'\nMSRP of the car : 25000\n')
        file.write(f'Total price - $400 bonus = ${total_price}')
        file.write(f'Subtotal with(4%) tax ={tax}')
        file.close()
    print('MSRP of the car : 25000')
    print(f'Total price - $400 bonus : $ {total_price}')
    print(f'Subtotal(4%) tax : ${tax}')
elif(color =='black' and brand == 'nissan' ):
    total_price = func.calculateprice_black(22000)
    tax = func.calculate_tax(total_price)
    print('---------Order summary-------')
    with open(path, 'a') as file:
        file.write(f'MSRP of the car : 22000')
        file.write(f'Total price with 25% discout = ${total_price}')
        file.write(f'Subtotal with(4%) tax ={tax}')
        file.close()
    print('MSRP of the car : 22000')
    print(f'Total price with 25% discount : $ {total_price}')
    print(f'Subtotal(4%) tax : ${tax}')
elif( color == 'white' and brand == 'nissan'):
    total_price = func.calculateprice_white(26000)
    tax = func.calculate_tax(total_price)
    print('---------Order summary-------')
    with open(path, 'a') as file:
        file.write(f'MSRP of the car : 26000')
        file.write(f'Total price - $400 bonus = ${total_price}')
        file.write(f'Subtotal with(4%) tax ={tax}')
        file.close()
    print('MSRP of the car : $26000')
    print(f'Total price - $400 bonus : $ {total_price}')
    print(f'Subtotal(4%) tax : ${tax}')
elif(color =='black' and brand == 'bmw' ):
    total_price = func.calculateprice_black(32000)
    tax = func.calculate_tax(total_price)
    print('---------Order summary-------')
    with open(path, 'a') as file:
        file.write(f'MSRP of the car : 32000')
        file.write(f'Total price with 25% discout = ${total_price}')
        file.write(f'Subtotal with(4%) tax ={tax}')
        file.close()
    print('MSRP of the car : 32000')
    print(f'Total price with 25% discount : $ {total_price}')
    print(f'Subtotal(4%) tax : ${tax}')
elif( color == 'white' and brand == 'bmw'):
    total_price = func.calculateprice_white(31000)
    tax = func.calculate_tax(total_price)
    print('---------Order summary-------')
    with open(path, 'a') as file:
        file.write(f'MSRP of the car : 31000')
        file.write(f'Total price - $400 bonus = ${total_price}')
        file.write(f'Subtotal with(4%) tax ={tax}')
        file.close()
    print('MSRP of the car : $31000')
    print(f'Total price - $400 bonus : $ {total_price}')
    print(f'Subtotal(4%) tax : ${tax}')
elif(color =='black' and brand == 'audi' ):
    total_price = func.calculateprice_black(46000)
    tax = func.calculate_tax(total_price)
    print('---------Order summary-------')
    with open(path, 'a') as file:
        file.write(f'MSRP of the car : 46000')
        file.write(f'Total price with 25% discout = ${total_price}')
        file.write(f'Subtotal with(4%) tax ={tax}')
        file.close()
    print('MSRP of the car : 46000')
    print(f'Total price with 25% discount : $ {total_price}')
    print(f'Subtotal(4%) tax : ${tax}')
elif( color == 'white' and brand == 'audi'):
    total_price = func.calculateprice_white(43000)
    tax = func.calculate_tax(total_price)
    print('---------Order summary-------')
    with open(path, 'a') as file:
        file.write(f'MSRP of the car : 43000')
        file.write(f'Total price with - $400 bonus = ${total_price}')
        file.write(f'Subtotal with(4%) tax ={tax}')
        file.close()
    print('MSRP of the car : 43000')
    print(f'Total price - $400 bonus : $ {total_price}')
    print(f'Subtotal(4%) tax : ${tax}')
elif(color =='black' and brand == 'honda' ):
    total_price = func.calculateprice_black(21000)
    tax = func.calculate_tax(total_price)
    print('---------Order summary-------')
    with open(path, 'a') as file:
        file.write(f'MSRP of the car : 21000')
        file.write(f'Total price with 25% discout = ${total_price}')
        file.write(f'Subtotal with(4%) tax ={tax}')
        file.close()
    print('MSRP of the car : 21000')
    print(f'Total price with 25% discount : $ {total_price}')
    print(f'Subtotal(4%) tax : ${tax}')
elif( color == 'white' and brand == 'honda'):
    total_price = func.calculateprice_white(25000)
    tax = func.calculate_tax(total_price)
    print('---------Order summary-------')
    with open(path, 'a') as file:
        file.write(f'MSRP of the car : 25000')
        file.write(f'Total price with - $400 bonus: ${total_price}')
        file.write(f'Subtotal with(4%) tax ={tax}')
        file.close()
    print('MSRP of the car : 25000')
    print(f'Total price - $400 bonus : $ {total_price}')
    print(f'Subtotal(4%) tax : ${tax}')
elif( color != 'black' or color != 'white' ):
    answer=input('Enter yes if the Customer is War veteran or disabled')
    if( str.upper(answer) == 'YES' ):
        discount_price = func.calculate_specialdiscount(28000)
        total_price = func.calculate_specialbonus(discount_price)
        tax = func.calculate_tax(total_price)
        print('---------Order summary-------')
        with open(path, 'a') as file:
            file.write(f'MSRP of the car : 28000')
            file.write(f'Total price with 25% discout = ${discount_price}')
            file.write(f'Total price with - $500 bonus: ${total_price}')
            file.write(f'Subtotal with(4%) tax ={tax}')
            file.close()
        print('MSRP of the car : 28000')
        print(f'Total price with 25% discount : $ {total_price}')
        print(f'Subtotal(4%) tax : ${tax}')
        print(f'Total price with 25% discount : {discount_price}')
        print(f'Total price - $500 bonus  : ${total_price}')
        print(f'Subtotal(4%) tax : ${tax}')

    else:
        cost=28000
        tax = func.calculate_tax(28000)
        print('---------Order summary-------')
        with open(path, 'a') as file:
            file.write(f'MSRP of the car : ${cost}')
            file.write(f'Subtotal with(4%) tax ={tax}')
            print(f'MSRP of the car : ${cost}')
            print(f'Subtotal(4%) tax : ${tax}')
else:
    print('invalid Entry')
#def car_total()


