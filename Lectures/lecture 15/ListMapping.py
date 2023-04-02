class Entry:
    def __init__(self, key, value):
        "Initializes a new entry w/ key and value"
        self.key = key
        self.value = value

    def __repr__(self):
        "String representation of entry"
        return f"Entry(key={self.key}, value={self.value})"

class ListMapping:
    def __init__(self, _L,):
        "Add data structure to store entries"
        self._L = []
    def __setitem__(self, k, v):
        "Add key:value pair to Mapping, or updated value if key already in mapping"
        new_entry = Entry(k, v)
        
        for e in self._L:
            if e.key == k:
                e.value = v
                return
            
        self._L.append(new_entry)
        
        
    def __getitem__(self, k):
        "Return value associated with key. Raise a KeyError if key is not in mapping"
        
        for e in self._L:
            if e.key == k:
                return e.value
        raise KeyError(f'key{k} not found in ListMapping')
    
class HashMapping:
    def __init__(self, _L,):
        "Add data structure to store entries"
        self.n_buckets = 8
        self._L = [[] for i in range(self.n_buckets)]
        self._len = 0
        
    def __len__(self):    
        return self._len        
    
    
    def find_bucket(self,key):
        return hash(key) % self.n_buckets
    
    def __setitem__(self, key, value):
        
        idx = self.find_bucket(key)
        
        for e in self._L [idx]:
            if e.key ==key:
                e.value =value
                return
            
            
            
        self._L[idx].append(Entry(key,value))
        
        #4 if I have to many items rehash
        
        