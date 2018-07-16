class SetofStacks():
     def __init__(self,threshold):
         self.items = []
         self.threshold = threshold

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         if len(self.items) and (len(self.items[-1]) < self.threshold):
            self.items[-1].append(item)
         else: self.items.append([item])

     def pop(self):
         last = self.items[-1]
         if len(self.items) == 0: return None

         v = last.pop()
         #if we popped off the only plate in the stack, then we have an empty stack at the end, which can be popped off
         if len(last) == 0: self.items.pop()
         return v



if __name__ == "__main__":
    stack = SetofStacks(3)
    stack.push(11)
    stack.push(22)
    stack.push(33)
    stack.push(44)
    stack.push(55)
    stack.push(66)
    stack.push(77)
    stack.push(88)
    print stack.pop()
    