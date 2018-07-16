class TreeNode():
  def __init__(self, data=None, left=None, right=None):
    self.data, self.left, self.right = data, left, right

class ListNode():
  def __init__(self, data=None, next=None,head=None):
    self.data, self.next = data, next
    self.head = head 
  def __str__(self):
    return str(self.data) + ',' + str(self.next)

  def add(self, val):
    if self.next == None:
        self.next = ListNode(val)
    else:
        self.next.add(val)


def Preorder(tree,arr,level):
  if tree:

    if len(arr)==level:
      node = ListNode(tree.data)
      arr.append(node)
    else:
      node = arr[level]
      node = node.add(tree.data)

    Preorder(tree.left,arr,level+1)
    Preorder(tree.right,arr,level+1)

  else: return

if __name__ == "__main__":
    node_h = TreeNode('H')
    node_g = TreeNode('G')
    node_f = TreeNode('F')
    node_e = TreeNode('E', node_g)
    node_d = TreeNode('D', node_h)
    node_c = TreeNode('C', None, node_f)
    node_b = TreeNode('B', node_d, node_e)
    node_a = TreeNode('A', node_b, node_c)

    lists=[]

    Preorder(node_a,lists,0)

    print str(lists[3])












 