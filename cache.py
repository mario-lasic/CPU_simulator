import collections

SIZE = 16

class Cache:
    def __init__(self) -> None:
        self.cache = collections.deque(maxlen = SIZE)
        