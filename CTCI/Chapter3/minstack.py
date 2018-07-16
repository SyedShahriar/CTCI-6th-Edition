class MinStack():
     def __init__(self):
         self.items = []
         self.mins = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         if item<=self.minVal():
             self.mins.append(item)
         self.items.append(item)

     def pop(self):
         if self.peek()==self.minVal(): self.mins.pop()
         return self.items.pop()

     def peek(self):
         if self.items: return self.items[-1]
         else: raise Exception('Stack is Empty')
         
     def minVal(self):
         if not self.mins: return float('inf')
         else: return self.mins[-1]

     def size(self):
         return len(self.items)


if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(5)
    min_stack.push(6)
    min_stack.push(3)
    min_stack.push(7)
    min_stack.pop()
    min_stack.pop()
    
    print min_stack.minVal()