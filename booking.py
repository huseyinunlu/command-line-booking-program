import csv
from io import StringIO
from os import write
import time
import datetime
from random import randrange
import re

class customers(object):
        ID = str
        name = str
        phoneNumber = str
        mail = str
        computerRes = str
        startDate = str
        endDate = str
        bookedDesk = int
        def asLine(self):
            return [self.ID, self.name, self.phoneNumber, self.mail, self.computerRes, self.startDate, self.endDate, str(self.bookedDesk)]
        

listOfCustomers = []


def readCSV():
    with open('customers.csv', "r", newline='\n') as csvfile:
        csvInput = csv.reader(csvfile)
        fieldnames = ['id', 'name', 'phoneNumber', 'mail', 'computerRes', 'startDate', 'endDate', 'bookedDesk']
        listOfCustomers.clear()
        for line in csvInput:
            if line !='':
                tempCustomer = customers()
                tempCustomer.ID = line[0]
                tempCustomer.name = line[1]
                tempCustomer.phoneNumber = line[2]
                tempCustomer.mail = line[3]
                tempCustomer.computerRes = line[4]
                tempCustomer.startDate = line[5]
                tempCustomer.endDate = line[6]
                tempCustomer.bookedDesk = int(line[7])
                listOfCustomers.append(tempCustomer)

def writeCSV():
    with open('customers.csv', "w", newline='') as csvfile:
        csvOutput = csv.writer(csvfile)
        for obj in listOfCustomers:
            csvOutput.writerow(obj.asLine())

def phoneControl(val):
    if(len(val)>=10):
        return val
    else:
        print("Phone number is not valid")
        phoneControl(input("Please enter a valid phone number: "))

def mailControl(val):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
    val = val.lower()
    if(re.search(regex, val)):
        return val
    else:
        print("Email is not valid")
        mailControl(input("Please enter a valid mail: "))

def computerReservedControl(val):
    if val == 'y':
        return 'Yes'
    elif val == 'n':
        return 'No'
    else:
        print("must be entered 'y' or 'n'")
        computerReservedControl(input("(y/n): "))

        



def dateControl(val, val2):
    format = "%d/%m/%Y"
    try:
        datetime.datetime.strptime(val, format)
        val1 = datetime.date(int(val.split("/")[2]),int(val.split("/")[1]),int(val.split("/")[0]))
    except ValueError:
        print("Start date of booking is invalid")
        dateControl(input("Enter valid date DD/MM/YYYY"), val2)
    if val1 > val2:
        return val
    else:
        print("Start date of booking is passed")
        return dateControl(input("Enter valid date DD/MM/YYYY"), val2)

def bookedDeskControl(val):
    if val.isdigit():
        return val
    else:
        print("Booked desk input in not valid")
        return dateControl(input("Enter booked desk"))
    

def viewBooking():
    readCSV()
    name = input("Enter name: ")
    isIdTrue = False
    for obj in listOfCustomers:
        if obj.name == name:
            print(obj.ID)
            isIdTrue = True
            print("ID: ",obj.ID)
            print("Name: ",obj.name)
            print("Phone Number: ",obj.phoneNumber)
            print("Mail: ",obj.mail)
            print("Computer Reserved: ",obj.computerRes)
            print("Booking Start Date: ",obj.startDate)
            print("Booking End Date: ",obj.endDate)
            print("Booked Desk:" , obj.bookedDesk)
    if isIdTrue == False:
        print("ID is invalid")
        viewBooking()
    input("Press ENTER to continue...")

def viewAllBookings():
    readCSV()
    for obj in listOfCustomers:
        print(obj.ID + ", "+ obj.name +", " + obj.phoneNumber+", "+ obj.mail+", "+ obj.computerRes+", "+obj.startDate+", "+obj.endDate+", " + str(obj.bookedDesk))
    input("Press ENTER to continue...")

def amendBooking():
    readCSV()
    name = input("Enter name: ")
    for obj in listOfCustomers:
        if obj.name == name:
            obj.name = input("Enter new name:")
            obj.phoneNumber = phoneControl(input("Enter new phone number:"))
            obj.mail = mailControl(input("Enter new mail:"))
            obj.computerRes = computerReservedControl(input("Computer Reserved(y/n):")) 
            obj.startDate = dateControl(input("Enter start date of booking:"), datetime.date.today())
            obj.endDate = dateControl(input("Enter end date of booking:"), datetime.date(int(obj.startDate.split("/")[2]),int(obj.startDate.split("/")[1]),int(obj.startDate.split("/")[0])))
            obj.bookedDesk = bookedDeskControl(input("Enter booked desk"))
        else:
            print("ID is invalid")
            viewBooking()
    writeCSV()

def createBooking():
    readCSV()
    tempCustomer = customers()
    tempCustomer.ID = str(randrange(0,9999))
    print("ID: ", tempCustomer.ID)
    tempCustomer.name = input("Enter new name:")
    tempCustomer.phoneNumber = phoneControl(input("Enter new phone number:"))
    tempCustomer.mail = mailControl(input("Enter new mail:"))
    tempCustomer.computerRes = computerReservedControl(input("Computer Reserved(y/n):")) 
    tempCustomer.startDate = dateControl(input("Enter start date of booking:"), datetime.date.today())
    tempCustomer.endDate = dateControl(input("Enter end date of booking:"), datetime.date(int(tempCustomer.startDate.split("/")[2]),int(tempCustomer.startDate.split("/")[1]),int(tempCustomer.startDate.split("/")[0])))
    tempCustomer.bookedDesk = bookedDeskControl(input("Enter booked desk"))
    listOfCustomers.append(tempCustomer)
    writeCSV()

def deleteBooking():
    readCSV()
    name = input("Enter name: ")
    for i in range(len(listOfCustomers)-1):
        if listOfCustomers[i].name == name:
            del listOfCustomers[i]
            break
    writeCSV()


def main():
    while True:
        print ("1- View a booking")
        print ("2- View all bookings")
        print ("3- Amend a booking")
        print ("4- Create a booking")
        print ("5- Delete a booking")
        print ("6- Quit the application")
        val = input ("->")

        if val == '1':
            viewBooking()
        elif val == '2':
            viewAllBookings()
        elif val == '3':
            amendBooking()
        elif val == '4':
            createBooking()
        elif val == '5':
            deleteBooking()
        elif val == '6':
            exit()
        else:
            print("Wrong Input")
            time.sleep(1)

            
if __name__ == "__main__":
    main()