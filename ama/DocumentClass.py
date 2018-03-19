#Document Class
#Author: Patrick Sellers
#Submitted Last: 3/18/18


class Document(object):

    ##listOfDocuments: list
    name = "null"
    url = "null"


    def __init__(self, n:str = "null", u:str = "null"):
        self.name = n
        self.url = u

    def getName(self) -> str:
        return self.name

    def getUrl(self) -> str:
        return self.url

    def setName(self, n:str):
        self.name = n

    def setUrl(self, u:str):
        self.url = u

    ##def addDocument(self, n:str, u:str):

    ##def delDocument(n:str):

    ##def displayDocList():

    def printDoc(self):
        print('name: ', self.name, "\n", 'URL: ', self.url)

##Test Lines:##
        
##x = Document()
##x.setUrl("www.cool.uk")
##x.getUrl()
##x.setName("Marketing Internship")
##x.getName()
##x.printDoc()
