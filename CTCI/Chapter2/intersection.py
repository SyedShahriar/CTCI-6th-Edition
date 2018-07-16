class Node():
    def __init__(self, data, next=None):
        self.data, self.next = data, next
    
    def __str__(self):
        string = str(self.data)
        if self.next:
            string += ',' + str(self.next)
        return string
    

class Solution(object):
    
    def intersection(self,head_a,head_b):
        
        if head_a==None or head_b ==None: return None
        
        node1 = head_a
        node2 = head_b
        size1=1
        size2=1
        
        while node1.next:
            node1=node1.next
            size1+=1
        while node2.next:
            node2=node2.next
            size2+=1
        
        if node1!=node2: return None
        
        longer = head_a if size1>size2 else head_b
        shorter = head_b if size2<size1 else head_a
        index = abs(size1-size2)
        
        while index and longer.next!=None:
            longer = longer.next
            index-=1
        
        while longer.next:
            if longer==shorter:
                return longer
            shorter=shorter.next
            longer= longer.next
            


if __name__ == "__main__":
    node = Node(70,Node(80))
    head1 = Node(10,Node(20,Node(30)))
    head2 = Node(20,Node(30,Node(40)))
    head3 = Node(50,Node(20,node))
    head4 = Node(60,Node(90,Node(10,node))) 
    
    print (Solution().intersection(head3,head4))

    
    