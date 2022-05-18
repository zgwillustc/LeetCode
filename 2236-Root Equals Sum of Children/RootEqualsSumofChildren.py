'''
You are given the root of a binary tree that consists of exactly 3 nodes:
the root, its left child, and its right child.

Return true if the value of the root is equal to the sum of the values of its
two children, or false otherwise.

Constraints:

The tree consists only of the root, its left child, and its right child.
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
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left.val + root.right.val


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
                 {'root': listToTree([10,4,6])
                  },
         'Output': True
         }

test1 = {'Input':
                 {'root': listToTree([5,3,1])
                  },
         'Output': False
         }

tests = [test0, test1]

def main():
    solution = Solution()
    evaluate(solution.checkTree, tests)

if __name__ == '__main__':
    main()
