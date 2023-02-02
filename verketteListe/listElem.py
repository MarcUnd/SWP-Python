class listElem:
    
    currElem = None
    nextElem = None
    
    def __init__(self, currElem, nextElem = None):
        self.currElem = currElem
        self.nextElem = nextElem
        pass
    
    def setNextElem(self, nextElem):
        if type(nextElem) == listElem:
            self.nextElem = nextElem
        else:
            self.nextElem = listElem(nextElem)
        
    def getNextElem(self):
        return self.nextElem
    
    def getCurrElem(self):
        return self.currElem
    
    def __str__(self) -> str:
        return str(self.currElem)
        