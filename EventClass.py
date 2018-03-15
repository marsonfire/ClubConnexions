from enum import Enum
class Repeat(Enum):
    NONE = 1
    WEEKLY = 2
    BIWEEKLY = 3
    MONTHLY = 4
    

class Event:

    name : str
    date : int
    time : int
    location : str
    description : str
    repetition:Repeat

    def _init_(self, n:str, d:int, t:int, l:int, d:str, r:Repeat):
        self.name = n
        self.date = d
        self.time = t
        self.location = l
        self.description = d
        self.repetition = r

    def getName(self) -> str:
        return self.name
    def getDate(self) -> int:
        return self.date
    def getTime(self) -> int:
        return self.time
    def getLocation(self) -> str:
        return self.location
    def getDescription(self) -> str:
        return self.description
    def getRepetition(self) -> Repeat:
        return self.repetition
    def setName(self, s:str):
        self.name = s
    def setDate(self, i:int):
        self.date = i
    def setTime(self, i:int):
        self.time = i
    def setLocation(self, s:str):
        self.location = s
    def setDescription(self, s:str):
        self.description = s
    def setRepeat(self, r:Repeat):
        self.repetition = r



        ##addEvent(name, date, time, location, description)
        ##deleteEvent(name)
        ##editEvent(name)
        ##displayEvent(name)
