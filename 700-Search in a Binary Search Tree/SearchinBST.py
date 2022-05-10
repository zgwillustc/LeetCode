'''
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the
subtree rooted with that node. If such a node does not exist, return null.

Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 10^7
root is a binary search tree.
1 <= val <= 10^7
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # My solution - Recursion
    # Time O(h) Space O(h)
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        if val == root.val:
            return root
        elif val > root.val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)

    # My solution - Iteration
    # Time O(h) Space O(1)
    def searchBST2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if val == root.val:
                return root
            elif val > root.val:
                root = root.right
            else:
                root = root.left
