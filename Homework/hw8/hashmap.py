class HashMap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity

 
    def hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self.hash(key)
        if not self.buckets[index]:
            self.buckets[index] = []
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)
                break
        else:
            self.buckets[index].append((key, value))
            self.size += 1
            
    def put(self, key, value):
        index = self.hash(key)
        if not self.buckets[index]:
            self.buckets[index] =[]
        for (k,v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index].append((key, value))
                break
          
    def get(self, key, default=None):
        index = self.hash(key)
        if not self.buckets[index]:
            return default
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return default

    def delete(self, key):
        index = self.hash(key)
        if not self.buckets[index]:
            return
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                del self.buckets[index][i]
                self.size -= 1
                return
        
    def __iter__(self):
        for bucket in self.buckets:
            if not bucket:
                continue
            for k,v in bucket:
                yield k,v