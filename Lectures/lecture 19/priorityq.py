class Entry:
    def __init__(self, priority, item):
        self.priority = priority
        self.item =  item

    def __lt__(self, other):
        #this is where you handle tie breaking
        return f'Entry({self.priority}, {self.item})'
class Heap:
    def __init__(self):
        self._L= []
        self._len = 0
        
    def add(self, priority, item):
        #append entry to end of list
        #upheap
        new_e = Entry(priority = priority, item =  item)
        
        self._L.append(new_e)
        self._L.upheap()
        
    def upheap(self, idx= None):
        if idx is None:
            idx = len(self) -1
        #do i have a parent
        idx_p = self.parent()
        #if so is the parent smaler
        if idx_p is None: return 
        #if so, swap and repeat
        while idx_p is not None and self._L[idx_p] < self._L[idx]:
            #swap items
            self._L[idx_p], self._L[idx] =  self._L[idx], self._L[idx_p]
            idx = idx_p
            idx_p = self.parent(idx_p)
            
  