from os import write
from data import menu
import time
import pandas as pd
import csv

#opening statement
print("V-Burger Point of sale terminal \n...")
time.sleep(1)
#employee ID number for identification
EmployeeID = input("Please Enter Your Employee ID: ")
print(EmployeeID + " \n...")
#active is status of program
active = True
custNum = 0 #custnum is order number

#fields in csv of logged orders
fields = ['Order Number','Employee','order','Total']
#writing to .csv
f = open('orderLog.csv','w', newline='')
write = csv.writer(f)
write.writerow(fields)

#loop that contains the majority of the function
while (active == True):

    custNum = custNum + 1 #incrementing each order number after an order
    foodItems = [] #array of all the food in an order
    price = [] #array of all the prices of that food
    print("Would the customer like an entree? \n (Y)es/(N)o: ")
    entree_choice = input() 
    entree_complete = False

    if entree_choice == 'Y' or entree_choice == 'y': #does the customer want an entree or not
        entree_complete = False
        while (entree_complete == False):  #loop going through the entree choices
            print(menu.ent)
            entreeNum = input("Which item would they like? (Item number): ")
            n = int(entreeNum)
            foodItems.append(menu.ent.iat[n-1,0]) #using the menu items from the other file's datadrame and calling them
            price.append(menu.ent.iat[n-1,1]) #same as above but for price
            print("Would you like to add another Entree? \n (Y)es (N)o: ")
            additional_entree = input()

            if additional_entree == 'Y' or additional_entree == 'y':
                print("Additional Entree Selection")
            elif additional_entree == 'N' or additional_entree == 'n':
                entree_complete = True
             
    
#side choice (same as entree but for side)
    print("Would the customer like an side? \n (Y)es/(N)o: ")
    side_choice = input()
    side_complete = False
    if (side_choice == 'Y' or side_choice =='y'):
        while (side_complete == False):
            print(menu.sid)
            sideNum = input("Which item would they like? (Item number): ")
            n = int(sideNum)
            foodItems.append(menu.sid.iat[n-1,0])
            price.append(menu.sid.iat[n-1,1])
            additional_side = input("Would you like to add another side? \n (Y)es (N)o: ")
            if (additional_side == 'Y' or additional_side == 'y'):
                print("Additional side Selection")
            elif additional_side == 'N' or additional_side == 'n':
                side_complete = True
                break

#drink choice (same as entree but for drink)
    print("Would the customer like a drink? \n (Y)es/(N)o: ")
    drink_choice = input()
    drink_complete = False
    if (drink_choice == 'Y' or drink_choice =='y'):
        while (drink_complete == False):
            print(menu.dri)
            drinkNum = input("Which item would they like? (Item number): ")
            n = int(drinkNum)
            foodItems.append(menu.dri.iat[n-1,0])
            price.append(menu.dri.iat[n-1,1])
            additional_drink = input("Would you like to add another drink? \n (Y)es (N)o: ")
            if (additional_drink == 'Y' or additional_drink == 'y'):
                print("Additional Drink Selection")
            elif additional_drink == 'N' or additional_drink == 'n':
                drink_complete = True
                break

    print("Your order is: ") 
    print(foodItems)
    print("Your total is: ")
    print(sum(price))

#Order Number','Employee','order','Total'
    rows = [custNum,EmployeeID,foodItems,sum(price)]
#writing to .csv
    write.writerow(rows)

    nextOrder = input("Are you ready for the next order? \n (Y)es/(N)o: ")
    if (nextOrder == 'Y' or nextOrder == 'y'):
        continue
    else:
        print("Have a great day!")
        break