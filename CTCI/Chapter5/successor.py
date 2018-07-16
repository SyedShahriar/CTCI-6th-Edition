class Node():
    def __init__(self,x=None):
        self.data = x
        self.left = None
        self.right = None

def successor(tree,val):
    prev = None 
    arr = []
    def inorder(root,value):       
        if root:
            inorder(root.right,value)
            
            inorder(root.left,value)

         
    inorder(tree,val)
    return prev



if __name__ == "__main__":
    n1 = Node(4)
    n2 = Node(10)
    n3 = Node(14)
    n4 = Node(22)
    n5 = Node(8)
    n6 = Node(12)
    n7 = Node(20)
    n6.left=n2
    n6.right=n3
    n5.left = n1
    n5.right = n6
    n7.left = n5
    n7.right = n4
    n8 = Node()
    
    print successor(n7,8)
    

