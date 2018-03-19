#from enum import Enum
#class Repeat(Enum):
#    NONE = 1
#    WEEKLY = 2
#    BIWEEKLY = 3
#    MONTHLY = 4
    

class Event(object):

    def __init__(self, name:str = 'null', date:str = 'null', time:str = 'null'
                 , location:int = 'null', description:str = 'null'):
        self.name = name
        self.date = date
        self.time = time
        self.location = location
        self.description = description
        #self.repetition = repitition

    def getName(self) -> str:
        return self.name
    def getDate(self) -> str:
        date = self.date
        month = date[:2]
        day = date[2:4]
        year = date[4:]
        return month + '/' + day + '/' + year
    def getTime(self) -> str:
        time = self.time
        hour = time[:2]
        minute = time[2:]
        return hour + ':' + minute
    def getLocation(self) -> str:
        return self.location
    def getDescription(self) -> str:
        return self.description
    #def getRepetition(self) -> Repeat:
    #    return self.repetition
    def setName(self, s:str):
        self.name = s
    def setDate(self, s:str):
        self.date = s
    def setTime(self, s:str):
        self.time = s
    def setLocation(self, s:str):
        self.location = s
    def setDescription(self, s:str):
        self.description = s
    #def setRepeat(self, r:Repeat):
    #    self.repetition = r
    def printEvent(self):
        print('name:', self.getName(), ', date:', self.getDate(),
              ', time:', self.getTime(), ', location:',
              self.getLocation(), ', description:', self.getDescription())
