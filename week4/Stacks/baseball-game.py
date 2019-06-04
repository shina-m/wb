class Stack:
        def __init__(self):
            self.items = []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            return self.items.pop()
        
        def peek(self, length):
            return self.items[-length:]

        def last_(self):
            return (self.items == [])

class Solution:
    
    def is_int(self, n):
        try:
            int(n)
        except ValueError:
            return False
        return True
    
    def calPoints(self, ops: List[str]) -> int:
        valid_points = Stack()
        total = 0
        
        for x in ops:
            if self.is_int(x):
                val = int(x)
                valid_points.push(val)
                total += val
                
            elif x == "+":
                val = sum(valid_points.peek(2))
                valid_points.push(val)
                total += val
                
            elif x == "D":
                val = sum(valid_points.peek(1)) * 2
                valid_points.push(val)
                total += val
                
            elif x == "C":
                val = valid_points.pop()
                total -= val
                
        return total
                
                
        