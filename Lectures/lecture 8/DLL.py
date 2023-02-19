class Node:
    'node for dll classes'
    def __init__(self, item, _next, _prev):
        'constructs a new node'
        self.item = item
        self._next = _next
        self._prev = _prev

    def __repr__(self):
        return f'Node '

class DoublyLinkedList:
    
    def __init__(self):
        'constructs a new (empty) dll'
        self._head = None
        self._tail = None
        self._len = 0

    def __len__(self):
        'returns the number of items in dll'
        return self._len

    def add_first(self, item): 
        #general case
        new_node= Node(item, _next =self._head, _prev =None)
        #update old head._prev
        self._head._prev =new_node

        #update dll._head
        self._head = new_node

        #increment length
        self._len += 1



    def remove_first(self):
        item =  self._head.item
        if len(self) !=: self._head._next._prev =  None
        else: self._tail = None 
        self._head = self._head._next
        self._len -= 1
        return item 



    def remove_last(self):
        #general case

        #extract item
        item = self._tail.item 
        #update old tail._prev's next pointer to None
        if len(self) != 1: self._tail._prev._next = None
        else: self._head = None
        #update tail 
        self._tail =self._tail._prev
        #decrement length
        self._len -= 1