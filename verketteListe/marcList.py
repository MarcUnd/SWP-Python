import listElem as le

class marcList:
    
    startElem = le.listElem('fünf')
    
    def __init__(self, startElem):
        self.startElem = le.listElem(startElem)
    
    
    def getLastItem(self):
        curr = self.startElem
        while not curr.getNextElem() == None:
            curr = curr.getNextElem()
        return curr
    
    def addItem(self, nextElem):
        self.getLastItem().setNextElem(nextElem)
    
    def isInList(self, item):
        curr = self.startElem
        while not curr == None:
            if item == curr:
                return True
            curr = curr.getNextElem()
        return False
    
    def getByIndex(self, index):
        curr = self.startElem
        count = 0
        while not curr == None:
            if count == index:
                return curr
            curr = curr.getNextElem()
            count += 1
        return None
    
    """
    def getIndex(self, item):
        curr = self.startElem
        count = 0
        while not curr == None:
            if item == str(curr):
                return count
            curr = curr.getNextElem()
            count += 1
        return None
    """
    
    def __str__(self) -> str:
        curr = self.startElem
        s = '*'+str(curr)
        while not curr.getNextElem() == None:
            curr = curr.getNextElem()
            s += ', ' + str(curr)
        return s+'*'
            