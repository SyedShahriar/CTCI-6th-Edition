class Node():
    def __init__(self, data, next=None):
        self.data, self.next = data, next
    
    def __str__(self):
        string = str(self.data)
        if self.next:
            string += ',' + str(self.next)
        return string
    

class Solution(object):
    
    def partition(self,head, pivot):
      a_head, a_tail = None, None
      b_head, b_tail = None, None
      node = head
      while node:
        print ('Given Head: '+str(node.data))
        if node.data < pivot:
          if a_head:
            a_tail.next, a_tail = node, node
            print('Intital a_head,a_tail: ' + str(a_tail.next.data) + ',' + str(a_tail.data))
          else:
            a_head, a_tail = node, node
        else:
          if b_head:
            b_tail.next, b_tail = node, node
          else:
            b_head, b_tail = node, node
        node = node.next

      a_tail.next = b_head
      return a_head
        

if __name__ == "__main__":
    head1 = Node(7,Node(2,Node(9,Node(1,Node(6,Node(3,Node(8)))))))

    print(str(Solution().partition(head1,6)))