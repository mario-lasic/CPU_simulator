import collections

SIZE = 16

class Cache:
    def __init__(self) -> None:
        self.cache = collections.deque(maxlen = SIZE)
        self.cache_flush()
        

def cache_flush(self):
    for i in range(SIZE):
        self.cache.append(("", ""))

def cache_search(self, address):
    for i in len(self.cache):
        if self.cache[i][0] == address:
            return self.cache[i][1]
    return None 

