# Filename: cwb3.py
# Author: Esther Tan
# Centre No / Index No: 3024 / 9
# Description: Append validated loan record to loan file

from classes import *
import datetime

def LOANRESOURCE():
    try:
        #open loan file to append 
        loan_file = open("LOAN.DAT", "a")
        
        #open updated resource file for reading (to check of resournceno exists)
        uresource_file = open ("URESOURCE.DAT", "r")

        #skip heading line from uresource file because first line of URESOURCE.DAT is the date (not required)
        heading_line = uresource_file.readline()

        #initialize resource number list
        ResourceNo_list = []
        
        #read record details
        detail_lines = uresource_file.readlines()

        #loop through each resource
        for resource_line in detail_lines:
                   
            #get ResourceNo
            ResourceNo = resource_line[0:5]

            #append resource number to resource number list
            ResourceNo_list.append(ResourceNo)

        #get and validate ResourceNo
        valid_ResourceNo = False
        while not valid_ResourceNo:
            ResourceNo = input("Enter resource number: ")
            if len(ResourceNo) == 0: #presence check
                print("Invalid! Empty input. Try again.")
            elif len(ResourceNo) != 5: #length check
                print("Invalid! Resource number must be 5 digits in length. Try again.")
            elif not ResourceNo.isdigit(): #data type check
                print("Invalid! Resource number must be in digits. Try again.")
            elif ResourceNo not in ResourceNo_list: #check if resource exists
                print("Error! Resource number does not exist. Try again.")
            else:
                valid_ResourceNo = True
            #assume resource is not loaned out already

        #get and validate StudentID
        valid_StudentID = False
        while not valid_StudentID:
            StudentID = input("Enter student ID: ")
            if len(StudentID) == 0: #presence check
                print("Invalid! Empty input. Try again.")
            elif len(StudentID) != 5: #length check
                print("Invalid! Student ID must be 5 characters in length. Try again.")
            #data type check (requires slicing in this case)
            elif not StudentID[0:1].upper() == 'S': #alternatively, can use studentid[0:1].lower() == 's':
                #characters (e.g. 's') use single quotes. strings (e.g. "hello") use double quotes.
                print("Invalid! First character of Student ID must be S.")
            elif not StudentID[1:5].isdigit(): #data type check
                print("Invalid! Last 4 characters of Student ID must be digits.")
            elif not 0 < int(StudentID[1:5]) < 10000:
                print("Invalid! Student ID must be between S0001 to S9999.")
            else:
                valid_StudentID = True
                
        #get and validate StudentName
        valid_StudentName = False
        while not valid_StudentName:
            StudentName = input("Enter student name: ")
            if len(StudentName) == 0: #presence check
                print("Invalid! Empty input. Try again.")
            elif len(StudentName) > 30: #length check
                print("Invalid! Student name cannot exceed 30 characters. Try again.")
            else:
                valid_StudentName = True
                
        #compute DateDueBack
        #get system current date
        DateLoaned = datetime.date.today()
        print("Date loaned:", DateLoaned)

        #add 7 days to get date due back
        DateDueBack = DateLoaned + datetime.timedelta(days=7)
        print("Date due:", DateDueBack)
        
        #format date due back to DDMMYY
        DateDueBack = DateDueBack.strftime("%d%m%y") #strftime reads a string and applies the desired format to what was previously specified
       
        #get and validate Evaluation
        valid_Evaluation = False
        while not valid_Evaluation:
            Evaluation = input("Enter evaluation: ")
            if len(Evaluation) == 0: #presence check
                print("Invalid! Empty input. Try again.")
            elif len(Evaluation) > 50: #length check
                print("Invalid! Evaluation cannot exceed 50 characters. Try again.")
            else:
                valid_Evaluation = True
                
        #write validated record to loan file
        loan = ("{0:5s}{1:5s}{2:30s}{3:6s}{4:30s}".format(ResourceNo, StudentID, StudentName, DateDueBack, Evaluation))
        loan_file.write(loan + "\n")

        #close files
        loan_file.close()
        uresource_file.close()

    except IOError:
        
        #display file input/output errors
        print("Error! Cannot read from input file or append to output file.")

#main
if __name__ == "__main__":
    LOANRESOURCE()
