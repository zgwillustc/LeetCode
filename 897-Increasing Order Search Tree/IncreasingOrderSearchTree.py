'''
Given the root of a binary search tree, rearrange the tree in in-order so that
the leftmost node in the tree is now the root of the tree, and every node has
no left child and only one right child.

Constraints:
The number of nodes in the given tree will be in the range [1, 100].
0 <= Node.val <= 1000
'''
# from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # My solution
    # Time O(n) Space O(n) - slow: two traversals
    def increasingBST2(self, root: TreeNode) -> TreeNode:
        current = root
        stack = []
        result = []
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
                continue
            current = stack.pop()
            result.append(current)
            current = current.right

        for i in range(len(result)-1):
            result[i].left = None
            result[i].right = result[i+1]
        result[-1].left = None
        result[-1].right = None
        return result[0]

    # My solution
    # Time O(n) Space O(h)
    def increasingBST(self, root: TreeNode) -> TreeNode:
        current = root
        stack = []
        newRoot = None
        pointer = None
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
                continue

            current = stack.pop()
            if not newRoot:
                newRoot = current
                pointer = current
            else:
                pointer.right = current
                pointer = current
                pointer.left = None
            current = current.right
        return newRoot

    # Inspired by the Solution
    # Time O(n) Space O(n)
    '''
    Approach 1: In-Order Traversal
    Intuition
    The definition of a binary search tree is that for every node, all the values of the left branch are less than the value at the root, and all the values of the right branch are greater than the value at the root.
    Because of this, an in-order traversal of the nodes will yield all the values in increasing order.
    Algorithm
    Once we have traversed all the nodes in increasing order, we can construct new nodes using those values to form the answer.
    '''
    def increasingBST3(self, root):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right

    # Time O(n) Space O(h)
    '''
    Approach 2: Traversal with Relinking
    Intuition and Algorithm
    We can perform the same in-order traversal as in Approach 1. During the traversal, we'll construct the answer on the fly, reusing the nodes of the given tree by cutting their left child and adjoining them to the answer.
    '''
    def increasingBST4(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right

    # Morris In-order traversal
    # Time O(n) Space O(1)
    def increasingBST5(self, node: TreeNode) -> TreeNode:
        dummy = tail = TreeNode()
        while node is not None:
            if node.left is not None:
                predecessor = node.left
                while predecessor.right is not None:
                    predecessor = predecessor.right

                predecessor.right = node
                left, node.left = node.left, None
                node = left
            else:
                tail.right = tail = node
                node = node.right

        return dummy.right

# Discussion
'''
https://leetcode.com/problems/increasing-order-search-tree/discuss/165885/C%2B%2BJavaPython-Self-Explained-5-line-O(N)
https://leetcode.com/problems/increasing-order-search-tree/discuss/958059/Python-Inorder-dfs-explained
https://leetcode.com/problems/increasing-order-search-tree/discuss/314557/100-faster-Easy-Python-Iterative-solution-without-the-dummy-tree-node
https://leetcode.com/problems/increasing-order-search-tree/discuss/958187/Morris-In-order-traversal-(Python-3-O(n)-time-O(1)-space)
https://leetcode.com/problems/increasing-order-search-tree/discuss/777069/Easy-Python-Solution-beats-90-with-Comments!
https://leetcode.com/problems/increasing-order-search-tree/discuss/280299/Iterative-Python-Solution-faster-than-98.56
'''

def listToTree(level_order: list) -> TreeNode:
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

# root = listToTree([5,3,6,2,4,None,8,1,None,None,None,7,9])
root = listToTree([2,1,4,None,None,3])

solution = Solution()
res = solution.increasingBST(root)
