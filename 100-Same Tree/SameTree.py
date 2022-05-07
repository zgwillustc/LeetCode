'''
Given the roots of two binary trees p and q, write a function to check
if they are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.

Constraints:
The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
'''
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # My solution - Recursion
    # Time O(n) n is a number of nodes in the tree, since one visits each node exactly once
    # Space O(log n) in the best case of complete balanced tree
    #       O(n) in the worst case of complete skewed tree
    def isSameTree2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif p and q:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

#        if p and q:
#            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
#        return p is q  # True if p==None and q==None else False

    # Iteration - DFS with stack
    def isSameTree3(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            n1, n2 = stack.pop()
            if n1 and n2 and n1.val == n2.val:
                stack.append((n1.left, n2.left))
                stack.append((n1.right, n2.right))
            elif n1 != n2:
                return False
        return True

    # Iteration - BFS with queue
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = [(p, q)]            # queue = collections.deque([(p, q)])
        while queue:
            n1, n2 = queue.pop(0)   # n1, n2 = queue.popleft()
            if n1 and n2 and n1.val == n2.val:
                queue.append((n1.left, n2.left))
                queue.append((n1.right, n2.right))
            elif n1 != n2:
                return False
        return True

def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Actual output:', actual)
        print('Expected output:', expect)
        print('Passed?', actual == expect)
        print('\n')

def listToTree(level_order: List) -> TreeNode:
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
                 {'p': listToTree([1,2,3]),
                  'q': listToTree([1,2,3])
                  },
         'Output': True
         }

test1 = {'Input':
                 {'p': listToTree([1,2]),
                  'q': listToTree([1,None,2])
                  },
         'Output': False
         }

test2 = {'Input':
                 {'p': listToTree([1,2,1]),
                  'q': listToTree([1,1,2])
                  },
         'Output': False
         }

test3 = {'Input':
                 {'p': None,
                  'q': None
                  },
         'Output': True
         }

tests = [test0, test1, test2, test3]

def main():
    solution = Solution()
    evaluate(solution.isSameTree, tests)

if __name__ == '__main__':
    main()
