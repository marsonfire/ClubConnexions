from EventClass import Event

class Calendar:

    listOfEvents = {}

    # note that two events cannot start at the same time
    def addEvent(self, e):
        key = e.getName()
        value = e
        self.listOfEvents[key] = e
    def deleteEvent(self, e):
        del self.listOfEvents[e.getName()]
    # this displays all the information about the event
    def displayEvent(self, e) -> str:
        display = ('The Event ' + e.getName() + ' is on ' + e.getDate()
                   + ' at ' + e.getTime() + ' in ' + e.getLocation() +
                   '. The following is a description of the event: ' +
                   e.getDescription())
        return display
    # this prints out each of the events in the calendar
    def printList(self):
        for key in self.listOfEvents:
            self.listOfEvents[key].printEvent()


