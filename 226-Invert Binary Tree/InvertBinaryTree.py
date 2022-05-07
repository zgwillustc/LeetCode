'''
Given the root of a binary tree, invert the tree, and return its root.

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
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
    # Time O(n)
    # Space O(h)
    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left = self.invertTree(root.left)
            root.right = self.invertTree(root.right)
            root.left, root.right = root.right, root.left
        return root

    # Iteration - BFS
    def invertTree3(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root

    # Interation - DFS
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.right)
                stack.append(node.left)
                
