'''
You are given the root of a binary tree where each node has a value 0 or 1.
Each root-to-leaf path represents a binary number starting with the most
significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent
01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from
the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.

Constraints:
The number of nodes in the tree is in the range [1, 1000].
Node.val is 0 or 1.
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf2(self, root: Optional[TreeNode]) -> int:
        # Time O(n) Space O(h)
        # Inspired by NeetCode
        def dfs(node, num):
            if not node:
                return 0
            num = num * 2 + node.val
            if node.left is None and node.right is None:
                return num
            return dfs(node.left, num) + dfs(node.right, num)

        return dfs(root, 0)

    # Inspired by Solution
    # DFS by Iteration (preorder)
    # Time O(n) Space O(h)
    def sumRootToLeaf3(self, root: Optional[TreeNode]) -> int:
        root_to_leaf = 0
        stack = [(root, 0)]
        while stack:
            node, current = stack.pop()
            if node is not None:
                current = current * 2 + node.val
                if node.left is None and node.right is None:
                    root_to_leaf += current
                else:
                    stack.append((node.right, current))
                    stack.append((node.left, current))
        return root_to_leaf

    # DFS by Recursion (preorder)
    def sumRootToLeaf4(self, root: Optional[TreeNode]) -> int:
        def preorder(r, curr_number):
            nonlocal root_to_leaf
            if r:
                curr_number = (curr_number << 1) | r.val
                # if it's a leaf, update root-to-leaf sum
                if not (r.left or r.right):
                    root_to_leaf += curr_number

                preorder(r.left, curr_number)
                preorder(r.right, curr_number)

        root_to_leaf = 0
        preorder(root, 0)
        return root_to_leaf

    # Morris Preorder Traversal
    # Time O(n) Space O(1)
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        root_to_leaf = curr_number = 0

        while root:
            # If there is a left child,
            # then compute the predecessor.
            # If there is no link predecessor.right = root --> set it.
            # If there is a link predecessor.right = root --> break it.
            if root.left:
                # Predecessor node is one step to the left
                # and then to the right till you can.
                predecessor = root.left
                steps = 1
                while predecessor.right and predecessor.right is not root:
                    predecessor = predecessor.right
                    steps += 1

                # Set link predecessor.right = root
                # and go to explore the left subtree
                if predecessor.right is None:
                    curr_number = (curr_number << 1) | root.val
                    predecessor.right = root
                    root = root.left
                # Break the link predecessor.right = root
                # Once the link is broken,
                # it's time to change subtree and go to the right
                else:
                    # If you're on the leaf, update the sum
                    if predecessor.left is None:
                        root_to_leaf += curr_number
                    # This part of tree is explored, backtrack
                    for _ in range(steps):
                        curr_number >>= 1
                    predecessor.right = None
                    root = root.right

            # If there is no left child
            # then just go right.
            else:
                curr_number = (curr_number << 1) | root.val
                # if you're on the leaf, update the sum
                if root.right is None:
                    root_to_leaf += curr_number
                root = root.right

        return root_to_leaf

def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Actual output:', actual)
        print('Expected output:', expect)
        print('Passed?', actual == expect)
        print('\n')

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

test0 = {'Input':
                 {'root': listToTree([1,0,1,0,1,0,1])
                  },
         'Output': 22
         }

test1 = {'Input':
                 {'root': listToTree([0])
                  },
         'Output': 0
         }

test2 = {'Input':
                 {'root': listToTree([0,None,1])
                  },
         'Output': 1
         }

test3 = {'Input':
                 {'root': listToTree([1,0,0])
                  },
         'Output': 4
         }

tests = [test0, test1, test2, test3]

def main():
    solution = Solution()
    evaluate(solution.sumRootToLeaf, tests)

if __name__ == '__main__':
    main()
