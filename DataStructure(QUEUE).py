class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item) 
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0) 
        return None
    
    def front(self):
        if not self.is_empty():
            return self.items  
        return None
    
    def is_empty(self):
        return len(self.items) == 0

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(f"Queue front: {queue.front()}") 
print(f"Queue dequeue: {queue.dequeue()}") 
