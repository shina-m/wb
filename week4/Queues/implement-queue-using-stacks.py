class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def is_empty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.items)

    
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.push(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.update_q()
        return self.stack2.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.update_q()
        print(self.stack1.items)
        print(self.stack2.items)
        return self.stack2.peek()
        
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.stack1.is_empty() and self.stack2.is_empty()
        
        
    def update_q(self):
        if self.stack2.is_empty():
            for _ in range(self.stack1.size()):
                self.stack2.push(self.stack1.pop())
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()