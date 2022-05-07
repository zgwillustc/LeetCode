'''
Given the root of a binary tree, construct a string consisting of parenthesis
and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping
relationship between the string and the original binary tree.

Constraints:
The number of nodes in the tree is in the range [1, 104].
-1000 <= Node.val <= 1000
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # My solution - recursion
    # Time O(n) Space O(h)
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)

        if right:
            return f'{root.val}('+left+')'+'('+right+')'
        elif left:
            return f'{root.val}('+left+')'
        else:
            return f'{root.val}'

    # Iteration
    def tree2str(self, root: Optional[TreeNode]) -> str:
        pass

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
                 {'root': listToTree([1,2,3,4])
                  },
         'Output': "1(2(4))(3)"
         }

test1 = {'Input':
                 {'root': listToTree([1,2,3,None,4])
                  },
         'Output': "1(2()(4))(3)"
         }

test2 = {'Input':
                 {'root': listToTree([1])
                  },
         'Output': '1'
         }

tests = [test0, test1, test2]

def main():
    solution = Solution()
    evaluate(solution.tree2str, tests)

if __name__ == '__main__':
    main()
