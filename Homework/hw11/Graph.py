import heapq

class Graph:

    def __init__(self, V=set(), E=dict()):
        self.V = V
        self.E = E

    def add_vertex(self, v):
        self.V.add(v)
        if v not in self.E:
            self.E[v] = dict()

    def remove_vertex(self, v):
        self.V.remove(v)
        for vertex in self.E:
            if v in self.E[vertex]:
                del self.E[vertex][v]
        del self.E[v]

    def add_edge(self, u, v, wt):
        self.add_vertex(u)
        self.add_vertex(v)
        self.E[u][v] = wt
        self.E[v][u] = wt

    def remove_edge(self, u, v, wt):
        if u in self.E and v in self.E[u] and self.E[u][v] == wt:
            del self.E[u][v]
            del self.E[v][u]

    def nbrs(self, v):
        return list(self.E[v].keys())

    def fewest_flights(self, city):
        visited = {city: None}
        queue = [(city, None)]
        
        while queue:
            current, prev = queue.pop(0)
            for neighbor in self.nbrs(current):
                if neighbor not in visited:
                    visited[neighbor] = current
                    queue.append((neighbor, current))
        
        tree = {}
        for city, prev in visited.items():
            if prev is not None:
                tree[city] = prev
        
        distances = {city: float('inf') for city in self.V}
        distances[city] = 0
        
        queue = [(0, city)]
        
        while queue:
            dist, current = heapq.heappop(queue)
            if dist > distances[current]:
                continue
            for neighbor in self.V[current]:
                weight = 1
                if distances[current] + weight < distances[neighbor]:
                    distances[neighbor] = distances[current] + weight
                    heapq.heappush(queue, (distances[neighbor], neighbor))
        
        return tree, distances
    
    def shortest_path(self, city):
        visited = {city: None}
        queue = [(city, None)]
        
        while queue:
            current, prev = queue.pop(0)
            for neighbor in self.nbrs(current):
                if neighbor not in visited:
                    visited[neighbor] = current
                    queue.append((neighbor, current))
        
        tree = {}
        for city, prev in visited.items():
            if prev is not None:
                tree[city] = prev
        
        distances = {city: float('inf') for city in self.V}
        distances[city] = 0
        
        queue = [(0, city)]
        
        while queue:
            dist, current = heapq.heappop(queue)
            if dist > distances[current]:
                continue
            for neighbor, weight in self.V[current].items():
                if distances[current] + weight < distances[neighbor]:
                    distances[neighbor] = distances[current] + weight
                    heapq.heappush(queue, (distances[neighbor], neighbor))
        
        return tree, distances
    
    def minimum_salt(self, city):
        visited = {city: None}
        queue = [(0, city, None)]
    
        while queue:
            dist, current, prev = heapq.heappop(queue)
            if current in visited:
                continue
            visited[current] = prev
            for neighbor, weight in self.V[current].items():
                heapq.heappush(queue, (dist + weight, neighbor, current))
    
        tree = {}
        for city, prev in visited.items():
            if prev is not None:
                tree[city] = prev
    
        distances = {city: float('inf') for city in self.V}
        distances[city] = 0
    
        for v1 in tree:
            v2 = tree[v1]
            weight = self.E[v1][v2]
            distances[v1] = weight
            if v2 in self.E:
                distances[v2] = 0
    
        queue = [(0, city)]
    
        while queue:
            dist, current = heapq.heappop(queue)
            if dist > distances[current]:
                continue
            for neighbor, weight in self.V[current].items():
                if distances[current] + weight < distances[neighbor]:
                    distances[neighbor] = distances[current] + weight
                    heapq.heappush(queue, (distances[neighbor], neighbor))
    
        return tree, distances