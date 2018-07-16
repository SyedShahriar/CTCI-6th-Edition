class Node():
    def __init__(self, data, next=None):
        self.data, self.next = data, next
    
    # def __str__(self):
    #     string = str(self.data)
    #     if self.next:
    #         string += ',' + str(self.next)
    #     return string
    

class Solution(object):
    
    def loopdetect(self,head):
        runner = head
        follower = head
        
        while runner and runner.next:
            runner= runner.next.next
            follower = follower.next
            if runner==follower: 
                print 
                break
        
        if runner==None or runner.next==None:
            return None
        
        follower = head
        
        while(follower!=runner):
            follower=follower.next
            runner=runner.next
        
        return runner


if __name__ == "__main__":
    node1 = Node(600)
    node2 = Node(700,Node(800,Node(900,node1)))
    node1.next = node2
    head2 = Node(500,node1)
    head1 = Node(100,Node(200,Node(300)))

    print (Solution().loopdetect(head2))

    
    