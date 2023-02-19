class LLNode: 
    def __init__(self, item, _next): #next is a reserved keyword so made private
        self.item = item
        self._next = _next

    def __repr__(self): #display code
        return f''

class LinkedList: 
    def __init__(self, items = None):
        self._head 