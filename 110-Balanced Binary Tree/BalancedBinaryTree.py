'''
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
    a binary tree in which the left and right subtrees of every node differ in
    height by no more than 1.

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # After NeetCode video
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return True, 0
            left, right = dfs(root.left), dfs(root.right) # can be further optimized. If left subtres is not balanced, no need to look at right subtree
            balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1

            return balanced, 1 + max(left[1], right[1])

        return dfs(root)[0]

    # After B2B video
    # Time O(n) Space O(h)
    def isBalanced2(self, root: Optional[TreeNode]) -> bool:
        result, _ = balancedHeight(root)
        return result

def balancedHeight(node): # can be further optimized. If left subtres is not balanced, no need to look at right subtree
    if not node:
        return True, -1
    left_bal, left_height = balancedHeight(node.left)
    if not left_bal:
        return left_bal, left_height
    right_bal, right_height = balancedHeight(node.right)
    if not right_bal:
        return right_bal, right_height
    height = max(left_height, right_height)+1
    return abs(left_height-right_height)<=1, height
#    return left_bal and right_bal and abs(left_height-right_height)<=1, height

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
                 {'root': listToTree([3,9,20,None,None,15,7])
                  },
         'Output': True
         }

test1 = {'Input':
                 {'root': listToTree([1,2,2,3,3,None,None,4,4])
                  },
         'Output': False
         }

test2 = {'Input':
                 {'root': listToTree([4,5,8,None,10,None,14,15])
                  },
         'Output': False
         }

test3 = {'Input':
                 {'root': None
                  },
         'Output': True
         }

tests = [test0, test1, test2, test3]

def main():
    solution = Solution()
    evaluate(solution.isBalanced, tests)

if __name__ == '__main__':
    main()
