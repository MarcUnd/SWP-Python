class doppelListElem:
    
    currElem = None
    nextElem = None
    prevElem = None
    
    def __init__(self, currElem, nextElem, prevElem) -> None:
        self.currElem = currElem
        self.nextElem = nextElem
        self.prevElem = prevElem