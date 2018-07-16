class Node():
  def __init__(self, data,next):
    self.data, self.next = data, next

class Solution(object):
    def kth_to_last(self, head,k):
        current = head
        node = head
        count=0
        while current!=None:
            count+=1
            current=current.next
        
        index = count-k
        
        while index>0:
            node=node.next
            index-=1
            
        return node
        
    #Alternate Solution using two pointers approach    
    def kth_to_last2(self,head, k):
        lead, follow = head, head
        for _ in xrange(k):
            if not lead:
                return None
            lead = lead.next
        while lead:
            lead, follow = lead.next, follow.next
        return follow    

if __name__ == "__main__":
    head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7,None)))))))
    print(Solution().kth_to_last(head,1).data)