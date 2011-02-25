# Filename: cwb2.py
# Author: Esther Tan
# Centre No / Index No: 3024 / 9
# Description: Read resource info from RESOURCE.DAT, get and validate extra details based on resource type, write to URESOURCE.DAT

from classes import *

def UPDATERESOURCE():
    try:
        #open resource file for reading
        resource_file = open("RESOURCE.DAT", "r")
        
        #open updated resource file for writing
        uresource_file = open ("URESOURCE.DAT", "w")

        #read heading line from resource file
        heading_line = resource_file.readline()
        heading_line = heading_line.rstrip("\n")
        
        #store creation date and number of records
        CreationDate = heading_line[0:10]
        NoOfRecords = heading_line[10:]
        
        #write creation date and number of records to updated resource file
        uresource_file.write(CreationDate + NoOfRecords + "\n")
        
        #get resource details
        detail_lines = resource_file.readlines()

        #initialize resource list
        resource_list = []
        
        #loop through each resource
        for record_line in detail_lines:

            #clean each record line
            record_line = record_line.rstrip("\n")
            
            #get and store record info
            ResourceNo= record_line[0:5]
            Title = record_line[5:35]
            DateAcquired = record_line[35:41]
            ResourceType = record_line[41:]
            
            #display resource info
            print("Resource no: " + ResourceNo)
            print("Title: " + Title)
            print("Date acquired: " + DateAcquired)
            print("Resource type: " + ResourceType)

            #if music CD
            if ResourceType == "C":
                #get and validate music CD details

                #get and validate artist
                valid_Artist = False
                while not valid_Artist:
                    Artist = input("Enter artist: ")
                    if len(Artist) == 0: #presence check
                        print("Invalid! Empty input. Try again.")
                    elif len(Artist) > 50: #length check
                        print("Invalid! Cannot exceed 50 characters. Try again")
                    else:
                        valid_Artist = True
                
                #get and validate number of tracks
                valid_NoOfTracks = False
                while not valid_NoOfTracks:
                    NoOfTracks = input ("Enter number of tracks: ")
                    if len(NoOfTracks) == 0:
                        print("Invalid! Empty input. Try again.")
                    elif not NoOfTracks.isdigit():
                        print("Invalid! Must be a number. Try again.")
                    elif not (0< int(NoOfTracks) <= 20):
                        print ("Invalid! Must be between 1 and 20. Try again.")
                    else:
                        NoOfTracks = NoOfTracks.zfill(3)
                        valid_NoOfTracks = True

##                #set null values to director and running time feilds
##                director = "NIL" + " " * 47
##                running_time = "NIL"
                
                #create music CD object and add to resource list
                resource_list.append(MusicCD(ResourceNo, Title, DateAcquired, ResourceType, Artist, NoOfTracks))

            #else (film DVD)
            else: #resource_type == "D"
                #get and validate film DVD details

                #get and validate director
                valid_Director = False
                while not valid_Director:
                    Director = input("Enter director: ")
                    if len(Director) == 0: #presence check
                        print("Invalid! Empty input. Try again.")
                    elif len(Director) > 50: #length check
                        print("Invalid! Cannot exceed 50 characters. Try again")
                    else:
                        valid_Director = True

                #get and validate running time
                valid_RunningTime = False
                while not valid_RunningTime:
                    RunningTime = input("Enter running time (in minutes): ")
                    if len(RunningTime) == 0: #presence check
                        print("Invalid! Empty input. Try again.")
                    elif not RunningTime.isdigit(): #data type check
                        print("Invalid! Must be a number. Try again.")
                    elif not (30 < int(RunningTime) <= 180): #range check
                        print("Invalid! Must be between 30 and 180 minutes. Try again.")
                    else:
                        valid_RunningTime = True

##                #set null values to artist and number of tracks feilds
##                artist = "NIL" + " " * 47
##                num_tracks = "NIL"

                #create film DVD object and add to resource list
                resource_list.append(FilmDVD(ResourceNo, Title, DateAcquired, ResourceType, Director, RunningTime))

        #write full resource details to updated resource file
##        Method 1
##        for resource in resource_list:
##            if resource.getResourceType() == "C":
##                uresource_file.write(resource.getResourceNo() +  resource.getTitle() + resource.getDateAcquired() + resource.getResourceType() + resource.getArtist() + resource.getNoOfTracks() + " " * 50 + "000" + "\n")
##
##            else: #film DVD
##                uresource_file.write(resource.getResourceNo() +  resource.getTitle() + resource.getDateAcquired() + resource.getResourceType() + " " * 50 + "00" + resource.getDirector() + resource.getRunningTime() + "\n")
                
##        Method 2
        for resource in resource_list:
            uresource_file.write(resource.display() + "\n") #polymorphism

##        #Method 3
##        uresource = ("{0:5s}{1:30s}{2:6s}{3:1s}{4:50s}{5:3s}{6:50s}{7:3s}".format(ResourceNo, Title, DateAcquired, ResourceType, Artist, NoOfTracks, Director, RunningTime) + "\n")
##        uresource_file.write(uresource + "\n")
        
        #close files
        resource_file.close()
        uresource_file.close()

    except IOError:
        
        #display file input/output errors
        print("Error! Cannot read from input file or write to output file.")

#main
if __name__ == "__main__":
    UPDATERESOURCE()
