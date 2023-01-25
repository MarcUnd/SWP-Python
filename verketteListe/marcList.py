import listElem as le

class marcList:
    
    def __init__(self, startElem=None, *args):
        self.startElem = le.listElem(startElem)
        for a in args:
            self.append(a)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.startElem:
            raise StopIteration
        else:
            item = self.startElem
            self.startElem = self.startElem.getNextElem()
            return item
    
    def last(self):
        curr = self.startElem
        while not curr.getNextElem() == None:
            curr = curr.getNextElem()
        return curr

    def first(self):
        return self.startElem
    
    def append(self, nextElem):
        self.last().setNextElem(nextElem)
    
    def contains(self, item):
        curr = self.startElem
        while not curr == None:
            if item == curr.currElem:
                return True
            curr = curr.getNextElem()
        return False
    
    def get(self, index:int):
        curr = self.startElem
        count = 0
        while not curr == None:
            if count == index:
                return curr
            curr = curr.getNextElem()
            count += 1
        raise Exception('Index out of bounds!')
   
    def index(self, item):
        curr = self.startElem
        count = 0
        while not curr == None:
            if item == curr.currElem:
                return int(count)
            curr = curr.getNextElem()
            count += 1
        raise Exception('Item not in list!')
    
    def pop(self, index:int):
        if index >= 0 and index <= self.index(self.last().currElem):
            if index == 0:
                self.startElem = self.get(index).getNextElem()
            else:
                self.get(index-1).setNextElem(self.get(index+1))
        else:
            raise Exception('Index out of bounds!')
                
    def remove(self, item):
        if self.contains(item):
            index = self.index(item)
            self.pop(index)
        else:
            raise Exception('Element not in list!')
    
    def count(self, item):
        curr = self.startElem
        count = 0
        while not curr == None:
            if item == curr.currElem:
                count += 1
            curr = curr.getNextElem()
        return count
            
    def extend(self, *args):
        for item in args:
            for i in item:
                self.append(i)
    
    def copy(self):
        newlist = marcList(self.startElem)
        lastIndex = self.index(self.last().currElem)
        for i in range(1,lastIndex+1):
            newlist.append(self.get(i))
        return newlist
    
    def insert(self, item, index):
        prev = self.get(index-1)
        nextItems = marcList(self.get(index))
        for i in range(index+1, len(self)):
            nextItems.append(self.get(i))
        prev.setNextElem(item)
        self.extend(nextItems)
            
    def __len__(self):
        curr = self.startElem
        count = 0
        while curr:
            curr = curr.getNextElem()
            count += 1
        return count
    
    def __str__(self) -> str:
        curr = self.startElem
        s = '*'+str(curr)
        while not curr.getNextElem() == None:
            curr = curr.getNextElem()
            s += ', ' + str(curr)
        return s+'*'
            