'''
'Effiency of linked list':

    'Access an Element:                  O(n)'
    'Add/remove at an iterator position: O(1)'
    'Add/remove first element:           O(1)'
    'Add last element:                   O(1)'
    'Remove last element:                O(n)'

'Effiency of doubly linked list':

    'Access an Element:                  O(n)'
    'Add/remove at an iterator position: O(1)'
    'Add/remove first element:           O(1)'
    'Add last element:                   O(1)'
    'Remove last element:                O(n)'
'''
class node: #wrapper, wraps over these nodes
    def __init__(self, data = None):
        'where we will store past data point or element to store node'
        self.data = data
        'store pointer to the next node'
        self.next= None #last element in the linked list so it will be set to none

class linked_list:
    def __init__(self): 
        'placeholder for the first pointer'
        self.head = node() 

    'used to create first element if empty and will add value last'
    def append(self,data):
        new_node = node(data)
        'node we are currently looking at'
        cur = self.head
        'saying while the next node exists'
        while cur.next != None:
            'will go through the list'
            cur = cur.next 
        'sets the next node equal to the new node'
        cur.next = new_node 
    
    'length of a linkedlist'
    def length(self):
        cur = self.head
        'total number of nodes seen'
        total = 0 #default will be zero 
        'while the next node exists iterate'
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    'helper function to display current contents of out list'
    def display(self):
        'list of elements we have seen'
        elems = []
        'will look at the first element in our current node'
        cur_node = self.head
        'while the next node exists iterate'
        while cur_node != None:
            cur_node = cur_node.next
            'sets elems equal to the nodes in the linked list'
            elems.append(cur_node.data)
        return elems


    def erase(self):
        if index >= self.length():
            print('index out of range')
            return 
        cur_idx = 0 
        cur_node = self.head
        while True :
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return 
            cur_idx += 1

            