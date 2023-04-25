import random
class Time:
    """A class that represents time in the format HH:MM"""
    def __init__(self, hour, minute):
        self.hour = int(hour)
        self.minute = int(minute)

    def __lt__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self < other, and False otherwise"""
        if self.hour < other.hour:
            return True
        elif self.hour == other.hour and self.minute < other.minute:
            return True
        else:
            return False
    
    def __eq__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self == other, and False otherwise"""
        if self.hour ==  other.hour and self.minute == other.minute:
            return True
        else:
            return False

    def __repr__(self):
        """Return the string representation of the time"""
        return f"{self.hour:02d}:{self.minute:02d}"

class Entry:
    """A class that represents a customer in the waitlist"""
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def __lt__(self, other):
        """Compare two customers based on their time, if equal then compare based on the customer name"""
        if self.time == other.time:
            return self.name < other.name
        return self.time < other.time
    

class Waitlist:#same thing as a heap
    def __init__(self):
        self._entries = []

    def add_customer(self, item, priority):#this code will follow the basic principle of a push method in a priority queue
        #TODO add customers to the waiting list.
        self._entries.append(Entry(item, priority))
        self.upheap(len(self._entries)-1)


    def peek(self):
        #TODO peek and see the first customer in the waitlist (i.e., the customer with the highest priority).
        '''check if entries is empty'''
        if not self._entries:
            return None
        '''extract the customer and time'''
        if self._entries == []: return None
        else: return (self._entries[0].name, self._entries[0].time)

        

    def seat_customer(self):
        # (i.e., the earliest reservation time) from the priority queue.
        if self._entries == []: return None
        # store the root node in a temporary variable
        temp = (self._entries[0].name, self._entries[0].time)
        # move bottom of heap (leaf) to root node
        self._entries[0] = self._entries[-1]
        self._entries.pop()
        self.downheap(0)
        return temp
        


    def print_reservation_list(self):
        '''Prints all customers in order of their priority (reservation time)'''
        # adding with seat_customer maintains the heap property
        temp_list = []
        while len(self._entries) > 0:
            temp_list.append(self.seat_customer())
        # adds entries back to original waitlist
        for i in temp_list:
            self._entries.append(Entry(i[0], i[1]))
        # return for testing purposes
        return temp_list

        
        
            
    def change_reservation(self, name, new_priority):
        #TODO Change the reservation time (priority) for the customer with the given name
        '''Change the reservation time (priority) for the customer with the given name'''
        # store current index of name
        for i in range(len(self._entries)-1):
            if name == self._entries[i].name:
                # store parent node for comparison
                p = self.parent(i)
                # set new priority
                self._entries[i].time = new_priority
                # if new entry is lighter than parent, upheap
                if p and self._entries[i] < self._entries[p]:
                    self.upheap(i)
                # if new entry is heavier than children, downheap
                else:
                    self.downheap(i)
                break      

    #Add other methods you may need
    def upheap(self,idx): 
       '''Upheap a customer added to the list to their correct index'''
       p = self.parent(idx)
        # if current node is less than parent node
       if idx > 0 and self._entries[idx] < self._entries[p]:
            # swap, then recursively upheap
            self._entries[idx], self._entries[p] = self._entries[p], self._entries[idx]
            self.upheap(p)

    def parent(self, i):
        if i <=0: return None
        return (i-1)//2
    
    def children(self, i):#might need to add edge cases to the following code
        left = 2 * i + 1
        right = 2 * i + 2
        return list(range(left, min(len(self._entries), right + 1)))
    
    def downheap(self,idx):
        c = self.children(idx)
        # if there is at least one child, find the child with the smallest value
        if c:
            child = min(c, key = lambda x: self._entries[x])
            # if the child's value is smaller than the current index's value, swap them
            if self._entries[child] < self._entries[idx]:
                self._entries[child], self._entries[idx] = self._entries[idx], self._entries[child]          
                # recursively call downheap on the swapped child to continue downheaping
                self.downheap(child)


