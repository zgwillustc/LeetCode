'''
Given the root of a Binary Search Tree (BST), return the minimum difference
between the values of any two different nodes in the tree.

Constraints:
The number of nodes in the tree is in the range [2, 10^4].
0 <= Node.val <= 10^5

Note: This question is the same as 530:
https://leetcode.com/problems/minimum-absolute-difference-in-bst/
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
    def minDiffInBST2(self, root: Optional[TreeNode]) -> int:
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

    pre = -float('inf')
    res = float('inf')

    def minDiffInBST(self, root):
        if root.left:
            self.minDiffInBST(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        if root.right:
            self.minDiffInBST(root.right)
        return self.res

    def minDiffInBST(self, root):
        if root is None:
            return

        self.minDiffInBST(root.left)
		# evaluate and set the current node as the node previously evaluated
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val

        self.minDiffInBST(root.right)
        return self.res

'''
I). In-order Traverse
| O(T): O(n) | O(S): O(h) | Rt: 28ms |

    def minDiffInBST(self, root: TreeNode) -> int:
        def inorder(node, pre, rst):
            if not node: return
            inorder(node.left, pre, rst)
            pre[0], rst[0] = node.val, min(rst[0], node.val - pre[0])
            inorder(node.right, pre, rst)

        pre, rst = [-float('inf')], [float('inf')]
        inorder(root, pre, rst)
        #BST size >= 2, solid result guaranted.
        return rst[0]
Alternative. woth global variable. | Rt: 28ms |

    pre, rst = -float('inf'), float('inf')
    def minDiffInBST(self, root: TreeNode) -> int:
        if not root: return
        self.minDiffInBST(root.left)
        self.pre, self.rst = root.val, min(self.rst, root.val - self.pre)
        self.minDiffInBST(root.right)
        return self.rst
II). Collect As List
| O(T): O(n) | O(S): O(n) | Rt: 24ms |

    def minDiffInBST(self, root: TreeNode) -> int:
        def inorder(node, rst):
            if not node: return
            inorder(node.left, rst)
            rst.append(node.val)
            inorder(node.right, rst)

        rst = []
        inorder(root, rst)
        return min(j - i for i, j in zip(rst, rst[1:]))
III). Post-order Traverse
| O(T): O(n) | O(S): O(h) | Rt: 32ms |

    def minDiffInBST(self, root: TreeNode) -> int:
        def postorder(node):
            if not node: return float('inf'), float('inf'), -float('inf')
            l, lmin, lmax = postorder(node.left)
            r, rmin, rmax = postorder(node.right)
            val = node.val
            return min(l, r, val - lmax, rmin - val), min(val, lmin), max(val, rmax)
        return postorder(root)[0]
Referrence: https://leetcode.com/problems/minimum-distance-between-bst-nodes/discuss/187735/Python-easy-to-understand-post-order-DFS-solution
Comment: compute from both end, record the sofar min and max values. Not trivial to understand, even harder to come up with.

IV). In-order Iteration with Visit State
| O(T): O(n) | O(S): O(n) | Rt: 16ms |

    def minDiffInBST(self, root: TreeNode) -> int:
        rst, pre, s = float('inf'), -float('inf'), [(root, 0)]
        while s:
            node, visited = s.pop()
            if not node: continue
            if not visited:
            	#adjust order
                s += [(node.right, 0), (node, 1), (node.left, 0)]
                continue
            pre, rst = node.val, min(rst, node.val - pre)
        return rst
Comment: in this iteration solution, all node will be visited in the order of in-order traverse (actually a sorted list from the perspective of value)

V). In-order Iteration with Pure Stack
| O(T): O(n) | O(S): O(n) | Rt: 20ms |

    def minDiffInBST(self, root: TreeNode) -> int:
        pre, rst, stack = -float('inf'), float('inf'), []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            pre, rst = node.val, min(rst, node.val - pre)
            root = node.right
        return rst
Comment: the inner while loop saves left -> parent in order, not included the right, but each time we pop a parent node, we switch to its right child, therefore the right child will be taken care after parent node, it is parent -> right. Put the inner while and pop together we have: left -> parent -> right, a perfect in-order traverse.
'''

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
    evaluate(solution.minDiffInBST, tests)

if __name__ == '__main__':
    main()
