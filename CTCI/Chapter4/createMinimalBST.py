class TreeNode(object):

	def __init__(self,x):
		self.data = x
		self.left = None
		self.right = None
	def __str__(self):
	    string = "(" + str(self.data)
	    if self.left:  string += str(self.left)
	    else:          string += "."
	    if self.right: string += str(self.right)
	    else:          string += "."
	    return string + ")"

def _createMinimalBST(arr):
	return createMinimalBST(arr,0,len(arr)-1)


def createMinimalBST(arr,start,end):
	if start>end:
		return None

	middle = (start + end)//2
	root = TreeNode(arr[middle])
	print middle+1
	root.left = createMinimalBST(arr,start,middle-1)
	root.right = createMinimalBST(arr,middle+1,end)
	return root

if __name__ == "__main__":
	sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	bst = _createMinimalBST(sorted_array)

	print bst



