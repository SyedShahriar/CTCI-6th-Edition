
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder (tree):
            if tree:
                inorder(tree.left)
                print tree.val
                self.vals.append(tree.val)
                inorder(tree.right)
        
        self.vals = []
        inorder(root)
        
        return self.vals

    def inorderTraversal2(self, root):
        def inorder2(tree):
            stack = []
            current  = tree
            run = True

            while run:
                if current:
                    stack.append(current)
                    current = current.left
                else:
                    if len(stack)>0:
                        current = stack.pop()
                        self.ans.append(current.val)
                        current = current.right
                    else:
                        run = False

        self.ans = []
        inorder2(root)
        return self.ans




if __name__ == "__main__":

    input_test = TreeNode(1)
    input_test.right = TreeNode(2)
    input_test.right.left = TreeNode(3)

    print(Solution().inorderTraversal2(input_test))

