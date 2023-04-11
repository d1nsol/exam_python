import heapq

class heapQueue:
    def __init__(self):
        self.data = []

    def push(self, value):
        heapq.heappush(self.data, value)

    def pop(self):
        if len(self.data) > 0:
            heapq.heappop(self.data)
        
    def top(self):
        if len(self.data) == 0:
            return -1
        else:
            self.data[0]