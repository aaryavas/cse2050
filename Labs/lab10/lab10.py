# This file empty on purpose - add the correct classes/methods below
class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority


    def __lt__(self, other):
        return self.priority < other.priority


    def __eq__(self, other):
        return self.priority == other.priority and self.item == other.item


class PQ_UL:
    def __init__(self):
        self.entries = []


    def __len__(self):
        return len(self.entries)


    def insert(self, item, priority):
        new_entry = Entry(item, priority)
        self.entries.append(new_entry)
        self.entries.sort()


    def find_min(self):
        if len(self.entries) == 0:
            raise Exception("Priority queue is empty")
        return self.entries[0]


    def remove_min(self):
        if len(self.entries) == 0:
            raise Exception("Priority queue is empty")
        return self.entries.pop(0)


class PQ_OL:
    def __init__(self):
        self.entries = []


    def __len__(self):
        return len(self.entries)


    def insert(self, item, priority):
        new_entry = Entry(item, priority)
        self.entries.append(new_entry)
        self.entries.sort()


    def find_min(self):
        if len(self.entries) == 0:
            raise Exception("Priority queue is empty")
        return self.entries[0]


    def remove_min(self):
        if len(self.entries) == 0:
            raise Exception("Priority queue is empty")
        return self.entries.pop(0)
