class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]
    
    
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = Queue()
        self.q2 = Queue()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        while not self.q2.is_empty():
            self.q1.enqueue(self.q2.dequeue())
            
        self.q1.enqueue(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        self.update_q()
        return self.q2.dequeue()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        self.update_q()
        return self.q2.peek()
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.q1.is_empty() and self.q2.is_empty()
        
    def update_q(self):
        if self.q2.is_empty():
            while True:
                r = self.q1.dequeue()
                if self.q1.is_empty():
                    self.q1.enqueue(r)
                    break
                else:
                    self.q2.enqueue(r)
                    
            self.q2, self.q1 = self.q1, self.q2
            
        
    
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()