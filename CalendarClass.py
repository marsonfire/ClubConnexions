import EventClass

class Calendar:

    dictionary

    ## note that two events cannot start at the same time
    def addEvent(e : Event):
        key = e.getName
        value = e
        dictionary[key] = e
    def deleteEvent(name : str):
        del dictionary[name]
    def displayEvent(e : Event) -> str:
        date = e.getDate
        month = date[:2]
        day = date[2:4]
        year = date[4:7]
        time = e.getTime
        hour = time[:2]
        minute = time[2:4]
        display = ('The Event ' + e.getName + ' is on ' + month + '/' + day + '/'
                   + '/' + year + ' at ' + hour + ':' + minute + ' in ' + e.getLocation
                   + '. The following is a description of the event: ' + e.getDescription)
        return display
