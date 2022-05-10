'''
Given the root of a Binary Search Tree (BST), return the minimum absolute
difference between the values of any two different nodes in the tree.

Constraints:
The number of nodes in the tree is in the range [2, 10^4].
0 <= Node.val <= 10^5

Note: This question is the same as 783:
https://leetcode.com/problems/minimum-distance-between-bst-nodes/
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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        return minDifference(root)[2]

def minDifference(node):
    'return the min val, max val and min difference of this tree with node as the root'
    if not node.left and not node.right:
        return node.val, node.val, float('inf')
    elif not node.left:
        right_minVal, right_maxVal, right_minDiff = minDifference(node.right)
        return node.val, right_maxVal, min(right_minVal-node.val, right_minDiff)
    elif not node.right:
        left_minVal, left_maxVal, left_minDiff = minDifference(node.left)
        return left_minVal, node.val, min(node.val-left_maxVal, left_minDiff)
    else:
        right_minVal, right_maxVal, right_minDiff = minDifference(node.right)
        left_minVal, left_maxVal, left_minDiff = minDifference(node.left)
        return left_minVal, right_maxVal, \
               min(node.val-left_maxVal, right_minVal-node.val,
                   left_minDiff, right_minDiff)

    def getMinimumDifference2(self, root: Optional[TreeNode]) -> int:
        L = []
        def dfs(node):
            if node.left: dfs(node.left)
            L.append(node.val)
            if node.right: dfs(node.right)
        dfs(root)
        return min(b - a for a, b in zip(L, L[1:]))

    def getMinimumDifference3(self, root: Optional[TreeNode]) -> int:
        def fn(node, lo, hi):
            if not node: return hi - lo
            left = fn(node.left, lo, node.val)
            right = fn(node.right, node.val, hi)
            return min(left, right)
        return fn(root, float('-inf'), float('inf'))

    def getMinimumDifference4(self, root: Optional[TreeNode]) -> int:
        self.previous = self.minimum = float('inf')

        def inorder(node):
            if node:
                inorder(node.left)
                self.minimum = min(self.minimum, abs(node.val-self.previous))
                self.previous = node.val
                inorder(node.right)

        inorder(root)
        return self.minimum


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
                 {'root': listToTree([4,2,6,1,3])
                  },
         'Output': 1
         }

test1 = {'Input':
                 {'root': listToTree([1,0,48,None,None,12,49])
                  },
         'Output': 1
         }

test2 = {'Input':
                 {'root': listToTree([23, None, 23])
                  },
         'Output': 0
         }

test3 = {'Input':
                 {'root': listToTree([236,104,701,None,227,None,911])
                  },
         'Output': 9
         }

tests = [test0, test1, test2, test3]

def main():
    solution = Solution()
    evaluate(solution.getMinimumDifference, tests)

if __name__ == '__main__':
    main()
