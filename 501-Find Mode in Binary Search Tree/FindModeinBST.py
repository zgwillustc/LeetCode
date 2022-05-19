'''
Given the root of a binary search tree (BST) with duplicates, return all the
mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:
    - The left subtree of a node contains only nodes with keys less than or
      equal to the node's key.
    - The right subtree of a node contains only nodes with keys greater than or
      equal to the node's key.
    - Both the left and right subtrees must also be binary search trees.

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-10^5 <= Node.val <= 10^5

Follow up: Could you do that without using any extra space? (Assume that the
implicit stack space incurred due to recursion does not count).
'''
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # My solution - Not use BST property 
    # Time O(n) Space O(n)
    def findMode1(self, root: Optional[TreeNode]) -> List[int]:
        result = {}
        def inOrder(node):
            if node:
                inOrder(node.left)
                result[node.val] = result.get(node.val, 0) + 1
                inOrder(node.right)
        inOrder(root)
        modes = []
        for val, freq in result.items():
            if not modes:
                modes.append(val)
            elif result[modes[-1]] == freq:
                modes.append(val)
            elif result[modes[-1]] < freq:
                modes.clear()
                modes.append(val)
        return modes

    # Discussion
    # Time O(n) Space O(1)
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        prev = None
        max_count = 0
        cur_count = 0
        result = []

        def dfs(node):
            nonlocal prev, max_count, cur_count, result
            if node:
                dfs(node.left)

                if node.val != prev:
                    cur_count = 1
                else:
                    cur_count += 1

                if cur_count == max_count:
                    result.append(node.val)
                elif cur_count > max_count:
                    result = [node.val]
                    max_count = cur_count
                prev = node.val

                dfs(node.right)

        dfs(root)
        return result




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
                 {'root': listToTree([1,None,2,2])
                  },
         'Output': [2]
         }

test1 = {'Input':
                 {'root': listToTree([0])
                  },
         'Output': [0]
         }

test2 = {'Input':
                 {'root': listToTree([5, 4, 6, 4, None, 6])
                  },
         'Output': [4,6]
         }

test3 = {'Input':
                 {'root': listToTree([2,1,3])
                  },
         'Output': [1,2,3]
         }

tests = [test0, test1, test2, test3]

def main():
    solution = Solution()
    evaluate(solution.findMode, tests)

if __name__ == '__main__':
    main()
