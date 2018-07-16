class Node():
	def __init__(self, left=None, right=None):
		self.left, self.right = left, right


def checkBalanced(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    def checkheight(tree):
        
        if tree==None: return 0

        left_height = checkheight(tree.left)

        right_height = checkheight(tree.right)

        height_diff = abs(left_height-right_height)

        if height_diff>1 or right_height==-1 or left_height==-1:
            return -1   

        return max(left_height,right_height)+1
    
    print checkheight(root)    
    return checkheight(root)!=-1


if __name__ == "__main__":
	Test = Node(Node(Node()),
    	Node(Node(Node()),Node()))

	print checkBalanced(Test)