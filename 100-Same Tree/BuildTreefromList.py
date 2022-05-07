from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# Below only works for building a complete tree
def insertValue(data: int, root: Optional[TreeNode], queue: List[TreeNode]):
    newNode = TreeNode(data)
    if queue:
        temp = queue[0]
    if root == None:
        root = newNode
    elif temp.left == None:
        temp.left = newNode
    elif temp.right == None:
        temp.right = newNode
        queue.pop(0)

    queue.append(newNode)
    return root

def listToCompleteTree(L: List[int], root: Optional[TreeNode] = None) -> Optional[TreeNode]:
    queue = []
    for i in L:
        root = insertValue(i, root, queue)
    return root

tree1 = listToCompleteTree([1,2])
#    1
#  /
#2
tree2 = listToCompleteTree([1,None,2])
#    1
#      \
#       2

#%%
def listToTree(level_order: List) -> TreeNode:
    values = iter(level_order)
    root = TreeNode(next(values))
    nodes_to_fill = [root]
    try:
        while True:
            next_node = nodes_to_fill.pop(0)
            new_left = next(values)
            if new_left is not None:
                next_node.left = TreeNode(new_left)
                nodes_to_fill.append(next_node.left)
            new_right = next(values)
            if new_right is not None:
                next_node.right = TreeNode(new_right)
                nodes_to_fill.append(next_node.right)
    except StopIteration:
        return root


tree1 = listToTree([1,2])
#    1
#  /
#2
tree2 = listToTree([1,None,2])
#    1
#      \
#       2
tree3 = listToTree([5,4,8,11,None,17,4,7,None,None,5,None,15])
#                      5
#                     /  \
#                    4    8
#                   /    / \
#                  11   17  4
#                 /      \   \
#                7        5   15

        