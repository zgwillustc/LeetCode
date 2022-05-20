'''
Given the root of an n-ary tree, return the postorder traversal of its nodes'
values.

Nary-Tree input serialization is represented in their level order traversal.
Each group of children is separated by the null value (See examples)

Constraints:
The number of nodes in the tree is in the range [0, 10^4].
0 <= Node.val <= 10^4
The height of the n-ary tree is less than or equal to 1000.

Follow up: Recursive solution is trivial, could you do it iteratively?
'''
from typing import Optional, List
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    # My solution - Recursion
    # Time O(n) Space O(n)
    def postorder1(self, root: Optional[Node]) -> List[int]:
        result = []

        def dfs(node):
            # nonlocal result
            if node:
                if node.children:
                    for child in node.children:
                        dfs(child)
                result.append(node.val)

        dfs(root)
        return result

    # Discussion
    # Iteration - reverse preorder traversal
    def postorder(self, root: Optional[Node]) -> List[int]:
        result = []
        if not root:
            return result

        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            stack.extend(node.children)
        return result[::-1]

    # Iteration - double append
    # https://leetcode.com/problems/n-ary-tree-postorder-traversal/discuss/881803/Python-iterative-method-easy-to-read.

    # https://leetcode.com/problems/n-ary-tree-postorder-traversal/discuss/165343/Python-Iterative-Solution-(without-reversing)%3A-same-stack-logic-as-recursive

    # Iteration - mark visited
    def postorder(self, root: Optional[Node]) -> List[int]:
        if not root:
            return []
        st = [(root,False)]

        ans = []
        while st:
            node,visited = st.pop()

            if visited:
                ans.append(node.val)
            else:
                st.append((node,True))

                for child in reversed(node.children):
                    st.append((child,False))
        return ans
