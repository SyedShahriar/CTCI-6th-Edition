class SortedStack():
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def isEmpty(self):
        return self.stack1 == []

    def push(self, item):

        while (self.stack1.peek()<item) and len(self.stack1)>0:
            self.stack2.push(self.stack1.pop())

        self.stack1.push(item)
        
        while len(self.stack2)>0:
            self.stack1.push(self.stack2.pop())

    def pop(self):
        return self.stack1.pop()

    def peek(self):
        return self.stack1.peek()

class Stack():
    def __init__(self):
        self.array = []
      
    def __len__(self):
        return len(self.array)
      
    def push(self, item):
        self.array.append(item)
      
    def pop(self):
        if not len(self.array): return None
        return self.array.pop()
    def peek(self):
        if not len(self.array): return None
        return self.array[-1]





if __name__ == "__main__":
    stack = SortedStack()
    stack.push(22)
    stack.push(11)
    stack.push(33)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(6)
    stack.push(88)
    print stack.pop()
    print stack.pop()
    print stack.pop()
    print stack.pop()
    print stack.pop()
    print stack.pop()
    print stack.pop()
    print stack.pop()
    