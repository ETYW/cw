# Filename: classes.py
# Author: Esther Tan
# Centre No / Index No: 3024 / 9
# Description: Support classes for music library

'''Superclass Resource'''
class Resource:

    '''Constructor'''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType):
        #self.__data is for private data
        self.__ResourceNo = ResourceNo
        self.__Title = Title
        self.__DateAcquired = DateAcquired
        self.__ResourceType = ResourceType

    '''Resource number accessor'''
    def getResourceNo(self):
        return self.__ResourceNo

    '''Title accessor'''
    def getTitle(self):
        return self.__Title

    '''Date acquired accessor'''
    def getDateAcquired(self):
        return self.__DateAcquired

    '''Resource type accessor'''
    def getResourceType(self):
        return self.__ResourceType

    #No '''Resource number modifier''' because primary key should not be edited
        
    '''Title modifier'''
    def setTitle(self, newTitle):
        self.__Title = newTitle

    '''Date acquired modifier'''
    def setDateAcquired(self, newDateAcquired):
        self.__DateAcquired = newDateAcquired

    '''Resource type modifier'''
    def setResourceType(self, newResourceType):
        self.__ResourceType = newResourceType

    '''Display helper function'''
    def display(self):
        return "{0:6s}{1:31s}{2:7s}{3}".format(self.getResourceNo(), self.getTitle(), self.getDateAcquired(), self.getResourceType())

#subclasses should be in the form: title-of-subclass(title-of-superclass)
'''Subclass MusicCD'''
class MusicCD(Resource): #(Resource) shows inheritance

    '''Constructor'''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType, Artist, NoOfTracks): # ResourceNo, Title, DateAcquired, ResourceType shows inheritance
        super().__init__(ResourceNo, Title, DateAcquired, ResourceType) #super() shows inheritance from superclass
        self.__Artist = Artist
        self.__NoOfTracks = NoOfTracks
    
    '''Artist accessor'''
    def getArtist(self):
        return self.__Artist

    '''Number of tracks accessor'''
    def getNoOfTracks(self):
        return self.__NoOfTracks

    '''Artist modifier'''
    def setArtist(self, newArtist):
        self.__Artist = newArtist

    '''Number of tracks modifier'''
    def setNoOfTracks(self, newNoOfTracks):
        self.__NoOfTracks = newNoOfTracks

    '''Display helper function'''
    def display(self):
        return "{0}{1:51}{2:}".format(super().display(), self.getArtist(), self.getNoOfTracks())

'''Subclass FilmDVD'''
class FilmDVD(Resource):

    #can use pass first to treat it as a dummy class

    '''Constructor'''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType, Director, RunningTime):
        super().__init__(ResourceNo, Title, DateAcquired, ResourceType)
        self.__Director = Director
        self.__RunningTime = RunningTime
    
    '''Director accessor'''
    def getDirector(self):
        return self.__Director

    '''Running time accessor'''
    def getRunningTime(self):
        return self.__RunningTime

    '''Director modifier'''
    def setDirector(self, newDirector):
        self.__Director = newDirector

    '''Running time modifier'''
    def setRunningTime(self, newRunningTime):
        self.__RunningTime = newRunningTime

    '''Display helper function'''
    def display(self):
        return "{0}{1:51}{2:}".format(super().display(), self.getDirector(), self.getRunningTime())

#main
##r1 = Resource("00001", "Best of Shinee", "030309", "C") #allocates storage and initializes values
##
##print(r1.getResourceNo())
##
##r1.setTitle("Shinee 2011") #to update values
##
##print(r1.getTitle())
##
##print(r1.display())
##
##r2 = Resource("00002", "", "", "")
##
##r2.setTitle("Super Junior Collection")
##r2.setDateAcquired("050510")
##r2.setResourceType("C")
##
##print(r2.display())
###print(r2.__Title) is illegal because private data should not be accessed directly
###private data can only be accessed through public methods
###this is known as data/information hiding (encapsulation)

##cd1 = MusicCD("00003", "FT Island Hits", "070708", "C", "FT Island", 10)
##
##print(cd1.getResourceNo()) #inherited method from superclass
##print(cd1.getArtist()) #class method belonging to musicCD class
##print(cd1.display()) #overriding
###cd1.display() will look for display method within musicCD class first
###if subclass has method, will call display() in subclass
###if subclass does not have the method, will check in superclass
###continues searching in grandparent class, greatgrandparent class etc.
###if method not found in any other class, error
##
##dvd1 = FilmDVD("00004", "New Shaolin Temple", "020211", "D", "Mr Andy", 120)
##
##print(dvd1.display())
##
resource_list = [] #initialize empty list
##
###adding to list
##resource_list.append(cd1)
###alternatively, resource_list.append(MusicCD("00003", "FT Island Hits", "070708", "C", "FT Island", 10)) will give the same result
##resource_list.append(dvd1)
##
##print(resource_list)

##for item in resource_list:
##    print(item.display()) #polymorphism

