# Filename: cwb4.py
# Author: Esther Tan
# Centre No / Index No: 3024 / 9
# Description: Append validated loan record to loan file

###read resource no, title, resource type into list of lists
##resource_list = [["00001", "The Planets Suite", "C"],
##                 ["00002", "Wuthering Heights", "D"]]
##
###read resource no, student id, student name, date due back, evaluation into list of lists
##loan_list = [["00001", "S0001", "Esther Tan", "200211", " " * 50],
##             ["00002", "S0001", "Esther Tan", "200211", "Returned" + " " * 42],
##             ["00003", "S0001", "Esther Tan", "010311", " " * 50]]
##
##ddb_list = []
##for loan in loan_list:
##    if loan[3] not in ddb_list:
##        ddb_list.append(loan[3])
##print(ddb_list)
##
##ddb_list = ["20-02-2011", "01-03-2011"]
##
##print(min(ddb_list))
##print(max(ddb_list))
##
###initialize dictionary of dates due back
##ddb_dict = {}
##
####for date_due_back in ddb_list:
####    ddb_dict[date_due_back] = 
##
###set up data structure to hold merged record
##final_rec = []
##
###compare resource no in loan_list with resource no in resource list
##for loan in loan_list:
##    for resource in resource_list:
##        if (loan[0] == resource[0]): #check if resource numbers coincide
##            if resource[2] == "C":
##                resource_type = "CD"
##            else:
##                resource_type = "DVD"
##            if loan[4] == (" " * 50):
##                final_rec.append([resource[0], resource[1], resource_type, loan[1], loan[2]])
##print(final_rec)
##
##
##'''----------------------------------------------------------------------------------------------------------------------------------------------------'''
from classes import *
import time

def REPORTRESOURCE():
    
    try:
        
        #open resource_file for input
        resource_file = open ("RESOURCE.DAT", "r")

        #initialize resource list (ResourceNo, Title, ResourceType)
        resource_list = []
        
        #read record details
        detail_lines = resource_file.readlines()

        #loop through each resource
        for resource_line in detail_lines:
                    
            #get resource number, title and resource type
            ResourceNo = resource_line[0:5]
            Title = resource_line[5:35]
            ResourceType = resource_line[41:42]

            #formatting resource type            
            if ResourceType == 'C':
                ResourceType = "CD"
            else:
                ResourceType = "DVD"

            #append ResourceNo, Title, ResourceType to resource list
            resource_list.append([ResourceNo, Title, ResourceType])
            
        #open loan file for input
        loan_file = open ("LOAN.DAT", "r")

        #initialize loan list (StudentID, StudentName, DateDueBack)
        loan_list = []
        
        #read record details
        detail_lines = loan_file.readlines()

        #loop through each resource
        for loan_line in detail_lines:

            #get student id, student name and date due back
            StudentId = loan_line[5:10]
            StudentName = loan_line[10:40]
            DateDueBack = loan_line[40:46]

            #formatting date due back
            DateDueBack = time.strptime(DateDueBack, "%d%m%y") #strptime reads a string, and divides it into day, month, and year
            DateDueBack = time.strftime("%d-%m-%Y", DateDueBack) #strftime reads a string and applies the desired format to what was previously specified

            #append StudentID, StudentName, DateDueBack to loan list
            loan_list.append([StudentId, StudentName, DateDueBack])

        #sort according to date due back
        #initialize DateDueBack list 
        DateDueBack_list = []
        #append DateDueBack to DateDueBack list
        DateDueBack_list.append(DateDueBack)

        #display report
##        Method 1
##        #initialize dictionary
##        FinalRecord = {}
##        #assign key and values to dictionary
##        FinalRecord[DateDueBack] = [ResourceNo, Title, ResourceType, StudentId, StudentName]
##        for DateDueBack in DateDueBack_list: 
##            for k, v in FinalRecord.items(): #k, v is the key and value respectively
##                print("Date:", k) #display date due back
##                for i in range (len(v)): #loop through list of resources
##                    for j in range (len(v[i])): #loop through list of loaned resource info
##                        print(v[i][j], end = "") #display loan resource info (ResourceNo, Title, ResourceType, StudentID, StudentName) on same line
##                    print() #go to new line to print next loan resource record
##                print("Number of resources:", len(v)) #display number of resources due on that day
            
##        Method 2
        #report list = ResourceNo, Title, ResourceType, StudentID, StudentName
        #report_list = resource_list + loan_list

        #initialize ResourceNo list for counting number of resources 
        ResourceNo_list = []

        #append ResourceNo to ResourceNo list
        ResourceNo_list.append(ResourceNo)

        #number of resources = count ResourceNo
        count = 0
        if ResourceNo in ResourceNo_list:
            count = count + 1        

        #loop to print report
        for DateDueBack in DateDueBack_list: 
            print("Date: " + DateDueBack)
            print("-" * 75)
            print("{0:6s}{1:31s}{2:4s}{3:6s}{4:31s}".format(ResourceNo, Title, ResourceType, StudentId, StudentName) + "\n")
        print("Number of resources: ", count)         
        
        #close files
        resource_file.close()
        loan_file.close()

    except IOError:
        
        #display file input/output errors
        print("Error! Cannot read from input file or append to output file.")

#main
if __name__ == "__main__":
    REPORTRESOURCE()
