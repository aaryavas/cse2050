import time


class stack:
    def __init__(self):
        self._L = []

    def push(self,item):
        self._L.append(item)

    def pop(self):
        return  self._L.pop()

    
    #attributes that start with l leading underscore are 'private' 
    #should ontl be accessed within this class


class stackSet:
    def __init__(self):
        self._S = set()

    def push(self,item):
        new_item = (time.time(), item)
        self._S.add(new_item)


    def pop(self):
        #find the most recent time stamp
        t_max = 0
        for item_tup in self.S:
            if item_tup[0] > t_max:
                t_max = item_tup[0]
                item_tup_max = item_tup
        
        return item_tup_max[1]




class Queue:
    'List wrapper'

    def __init__(self):
        self._L = []
    
    def enqueue(self, item):
        'add item to end of queue'
        self._L.append(item)

    def dequeue(self):
        'remove and return an item form beginning od queue'
        return self._L.pop(0)