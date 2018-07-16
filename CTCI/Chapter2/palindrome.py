class Node():
    def __init__(self, data, next=None):
        self.data, self.next = data, next
    
    def __str__(self):
        string = str(self.data)
        if self.next:
            string += ',' + str(self.next)
        return string
    

class Solution(object):
    
    def is_palindrome(self,head):
        node = head
        node2 = head
        chars = []
        reversed_chars = []
        
        while node!=None:
            chars.append(node.data)
            node = node.next
        
        while node2:
            if node2.data!=chars.pop():
                return False
            node2 = node2.next
        
        return True
        
    
    def is_palindrome2(self,head):
       reversed_head = Solution().reverseList(head)
       
       while head and reversed_head:
           if (head.data != reversed_head.data):
               return False
           head = head.next
           reversed_head = reversed_head.next
       return True
    
    def reverseList(self,node):
        #create one null node holding the prev value
        #set curr node to the head
        prev = None
        curr = node
        
        while curr:
            #get the next node after current
            nex = curr.next
            #change the pointer to point from current to next, to point current to previous
            curr.next = prev
            #set prev to current
            prev = curr
            #set current to next
            curr = nex
        node = prev
        return node
            


if __name__ == "__main__":
    head1 = Node('r',Node('a',Node('c',Node('e',Node('c',Node('a',Node('b')))))))

    print(Solution().is_palindrome(head1))

    
    