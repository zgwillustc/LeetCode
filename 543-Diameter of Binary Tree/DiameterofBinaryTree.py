'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges
between them.

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
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
    # Watched the Youtube video - https://www.youtube.com/watch?v=bkxqA8Rfv04
    # The diameter of a node in a tree = height of left subtree + height of right subtree + 2
    # Time O(n) Space O(h)
    def diameterOfBinaryTree2(self, root: Optional[TreeNode]) -> int:
        res = 0  # res = [0]
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            nonlocal res   # no need if claim res = [0] at first (but may be not a good practice)
            res = max(res, 2+left+right) # res[0] = max(res[0], 2+left+right)
            return 1 + max(left, right)
        dfs(root)
        return res    # return res[0]

    def diameterOfBinaryTree3(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0   # This works like a "global" variable (but not a good practice)

        def height(node):
            if not node: return -1
            left, right = height(node.left), height(node.right)
            self.diameter = max(self.diameter, 2+left+right)
            return 1 + max(left, right)

        height(root)
        return self.diameter

    # The diameter is the maximum of either:
    # Passing through the root (in which case the longest path would be using the maximum depth of left and right child)
    # The diameter of the left child
    # The diameter of the right child
    def diameterOfBinaryTree(self, root):
        return self.diameter_rec(root)[0]

    def diameter_rec(self, root):
        if not root:
            return 0, -1

        left_diameter, left_height = self.diameter_rec(root.left)
        right_diameter, right_height = self.diameter_rec(root.right)
        return (max(left_diameter, right_diameter, left_height + right_height + 2), max(left_height, right_height) + 1)

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
                 {'root': listToTree([1,2,3,4,5])
                  },
         'Output': 3
         }

test1 = {'Input':
                 {'root': listToTree([1,2])
                  },
         'Output': 1
         }

test2 = {'Input':
                 {'root': listToTree([2, 3, None, 1])
                  },
         'Output': 2
         }

test3 = {'Input':
                 {'root': listToTree([3,5,None,6,7,None,None,4,None,None,8])
                  },
         'Output': 4
         }

tests = [test0, test1, test2, test3]

def main():
    solution = Solution()
    evaluate(solution.diameterOfBinaryTree, tests)

if __name__ == '__main__':
    main()
