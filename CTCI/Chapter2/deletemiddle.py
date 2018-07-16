class Node():
  def __init__(self, data,next):
    self.data, self.next = data, next

class Solution(object):
    
    def deletemiddle(self,mid):
        next = mid.next
        mid.data= next.data
        mid.next= next.next
        

if __name__ == "__main__":
    head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7,None)))))))
    print head.next.next.data
    Solution().deletemiddle(head.next.next)
    print head.next.next.data