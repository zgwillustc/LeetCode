# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # My solution - Recursion - Depth first search
    # Time O(n) Space O(n)  worst case for skewed trees
    def maxDepth(self, root: TreeNode) -> int:
        return self.helper(root)

    def helper(self, node):
        if not node:
            return 0
        return 1 + max(self.helper(node.left), self.helper(node.right))

    # My previous solution
    def maxDepth0(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # Breadth first search
    # To be done
    
    # Iteration
    # To be done
    

root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20, TreeNode(15), TreeNode(7))

root2 = TreeNode(1, None, TreeNode(2))

root3 = None

def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print(':', actual == expect)

test0 = {'Input':
                 {'root': root1
                  },
         'Output': 3
         }

test1 = {'Input':
                 {'root': root2
                  },
         'Output': 2
         }

test2 = {'Input':
                 {'root': root3
                  },
         'Output': 0
         }

tests = [test0, test1, test2]

def main():
    solution = Solution()
    evaluate(solution.maxDepth, tests)

if __name__ == '__main__':
    main()
