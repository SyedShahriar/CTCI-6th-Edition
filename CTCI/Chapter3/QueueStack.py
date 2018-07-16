class QueueStack():
     def __init__(self):
         self.stack1 = Stack()
         self.stack2 = Stack()

     def isEmpty(self):
         return self.stack1 == []

     def push(self, item):
        self.stack1.push(item)

     def remove(self):

        if len(self.stack2)==0:
            while len(self.stack1):
                self.stack2.push(self.stack1.pop())

        #alternate way of doing it

        # while len(self.stack1)!=1:
        #     self.stack2.push(self.stack1.pop())

        #first_item = self.stack1.pop()

        # while self.stack2:
        #     self.stack1.push(self.stack2.pop())

        # return first_item

        return self.stack2.pop()



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
    stack = QueueStack()
    stack.push(11)
    stack.push(22)
    stack.push(33)
    stack.push(44)
    stack.push(55)
    stack.push(66)
    stack.push(77)
    stack.push(88)
    print stack.remove()
    print stack.remove()
    