import os
import platform
import datetime

def exit_Prog():
    user_Inp = input("Do you want to exit this program ? (Y/N) : ").lower()
    if user_Inp == "y":
        print("Thank you for using my program")
    elif user_Inp == "n":
        main_Menu()
    else:
        print("You have entered an incorrect key.......try again")
        main_Menu()
        
def directory():
    listDir = os.listdir()
    print(listDir)
    main_Menu()

def create_File():
    fileName = input('Enter the file name : ')
    newFile = open(fileName,"w")
    main_Menu()

def new_Dir():
    dirName = input('Enter the name of the directory that you want to create : ')
    newDir = os.mkdir(dirName)
    main_Menu()



def start_ping():
    x = "www.google.com"

    a = input("Enter the server you want to ping : ")
    if a =="":
        hostname = "www.google.com"
        pingResponse = os.system("ping -c 6 " + hostname +" > pingresults.txt" )
        print("Pinging  "+ hostname +"  ended at "+str(datetime.datetime.now()))
        main_Menu()
    
    
    else:
        hostname = a
        pingResponse = os.system("ping -c 6 " + hostname +" > pingresults.txt" )
        print("Pinging  "+ hostname +"  ended at "+str(datetime.datetime.now()))
        main_Menu()
    
def rem_Files():
    user_Inp = input("Are you sure that you want to remove all the files  ? (Y/N) : ").lower()

def system_Info():
    systemInfo = os.system("system_profiler SPHardwareDataType")
    print(systemInfo)
    main_Menu()

def main_Menu():
    print("""\t  *************************************************************\n
          1. List Directories - List the directories in the current location.\n
          2. Create a file - Create a new file with a given name and extension.\n
          3. Create a directory - Create a new directory with a given name.\n
          4. Ping a server - Ping a server (default: google.com) and optionally save the output to a textfile.\n
          5. Print system information\n
          6. Exit - Exit the application.\n
          *****************************************************************\n""")
    
    userChoice = input("Enter the selection\n")
        
    match (int(userChoice)):
        case 1:
            return directory()
        case 2:
            return create_File()
        case 3:
            return new_Dir()
        case 4:
            return start_ping()
        case 5:
            return system_Info()
        case 6:
            return exit_Prog()
        case _:
            print("You have entered an incorrect key.......try again")
            return main_Menu()
    
main_Menu()