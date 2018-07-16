class Node():
  def __init__(self, data, next):
    self.data = data
    self.next = next

class Solution(object):
    def remove_duplicates(self, head):
        current = head
        hashtable = {current.data:True}
        while current.next!=None and current!=None:
            if current.next.data in hashtable.keys():
                current.next=current.next.next
            else:
                hashtable[current.next.data]=True
                current=current.next
        return head

if __name__ == "__main__":
    head = Node(3,Node(3,Node(3,Node(3,Node(5,None)))))
    Solution().remove_duplicates(head)