# Filename: cwb1.py
# Author: Esther Tan
# Centre No / Index No: 3024 / 9
# Description: Read data from RESOURCE.DAT, format and output to screen

#RESOURCE.DAT file should use fonts with equal width characters (e.g. Courier New) to prevent confusion when reading characters

import time

def DISPLAYRESOURCE():
    
    try:
        #open file for reading
        resource_file = open("RESOURCE.DAT", "r")
        
        #read in first line (creation date and number of records)
        heading_line = resource_file.readline()
        heading_line = heading_line.rstrip("\n") #rstrip = right stip: removes white space to the right of last character
        
        #store creation date and number of records
        CreationDate = heading_line[0:10] #[0:10] reads first 10 characters (i.e. creation date). Can also be [:10] which reads from the start till the 10th character
        NoOfRecords = heading_line[10:] #[10:] reads characters from the 10th character onwards
        #note: [x:y] is inclusive of x, exlusive of y
        
        #display heading lines with creation date and number of records
        print("Creation date: " + CreationDate)
        print("#Resources: " + NoOfRecords)
        
        #display subheadings
        print("{0:13s}{1:15s}{2:32s}{3:}".format("Resource No", "Resource Type", "Title", "Date Acquired"))
        #"".format should contain the placeholders (reserves space for each input required)
        #{0:13s} reserves 13 character spaces for the first input (Resource No), read as a string
        #{1:17s} reserves 17 character spaces for the second input (Resource Type), read as a string
        #{2:35s} reserves 35 character spaces for the third input (Title), read as a string
        #note: Date Acquired does not need any specific number of characters for placeholder since it is at the end of the line

        print("-" * 75)

        #read in all record detail lines
        detail_lines = resource_file.readlines()
        
        #loop through number of records
        for record_line in detail_lines:

            #read record detail line
            record_line = record_line.rstrip("\n")
            
            #store resource no, title, date acquired and resource type
            ResourceNo = record_line[0:5] 
            Title = record_line[5:35]
            DateAcquired = record_line[35:41]
            ResourceType = record_line[41:]

            #format date from DDMMYY to DDMMYYYY
            #note: lowercase y gives year in 2 characters, uppercase y gives year in 4 characters
            DateAcquired = time.strptime(DateAcquired, "%d%m%y") #strptime reads a string, and divides it into day, month, and year
            DateAcquired = time.strftime("%d-%m-%Y", DateAcquired) #strftime reads a string and applies the desired format to what was previously specified

            #format and display record detail line
            print("{0:13s}{1:15s}{2:32s}{3:}".format(ResourceNo, ResourceType, Title, DateAcquired))
            
        #close file
        resource_file.close()

    except IOError:
        #display input file error
        print("Error! Input file does not exist or is corrupted.")

#main program (used to call out the relevant files)
if __name__ == "__main__":
    DISPLAYRESOURCE()
