'''
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Constraints:
The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
'''
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stack = [(root, '')]
        res = []

        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                res.append(path + str(node.val))
            if node.left:
                stack.append((node.left, path + str(node.val) + '->'))
            if node.right:
                stack.append((node.right, path + str(node.val) + '->'))

        return res

    # Time O(n) Space O(n)
    def binaryTreePaths2(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        dfs(root, '', paths)
        return paths

def dfs(node, path, paths):
    path += str(node.val)

    if node.left == None and node.right == None:
        paths.append(path)
        return
    if node.left:
        dfs(node.left, path + '->', paths)
    if node.right:
        dfs(node.right, path + '->', paths)

# https://leetcode.com/problems/binary-tree-paths/discuss/68272/Python-solutions-(dfs%2Bstack-bfs%2Bqueue-dfs-recursively).
# https://leetcode.com/problems/binary-tree-paths/discuss/68507/8-lines-in-python48ms

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
                 {'root': listToTree([1,2,3,None,5])
                  },
         'Output': ["1->2->5","1->3"]
         }

test1 = {'Input':
                 {'root': listToTree([1])
                  },
         'Output': ['1']
         }

test2 = {'Input':
                 {'root': listToTree([1,2,3,4,5,None,6])
                  },
         'Output': ['1->2->4','1->2->5','1->3->6']
         }

test3 = {'Input':
                 {'root': listToTree([1,2])
                  },
         'Output': ['1->2']
         }

tests = [test0, test1, test2, test3]

def main():
    solution = Solution()
    evaluate(solution.binaryTreePaths, tests)

if __name__ == '__main__':
    main()
